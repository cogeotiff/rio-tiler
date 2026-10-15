# Plan: offload blocking GDAL/numpy work from the async readers

Branch `async-offload-warp`.

## Prompts

### Prompt 1
> the async reader AsyncArrayReader uses `sync` GDAL code for the reprojection (see _warp.py)
> should I use something like https://github.com/fastapi/asyncer to avoid blocking the event loop?

### Prompt 2
> ok let's work on this
> start a new branch and do relatively small commits
> avoid breaking change and refactor

### How the prompts shaped the plan
- Prompt 1: use the standard library (`asyncio.to_thread`) instead of adding `asyncer`/`anyio`.
- Prompt 2: one helper and one commit per reader. The public API and the method signatures stay the same, and the existing code is not reorganized. Only the blocking calls are wrapped.

## Context
`rio_tiler.experimental.geotiff.Reader` and `rio_tiler.experimental.zarr.AsyncArrayReader` read data asynchronously, then post-process it with synchronous code:

- `part()` → `rio_tiler._warp.warp` (`rasterio.warp.reproject` plus `resize_array`, looped over 2048px output tiles);
- `preview()` → `ImageData.reproject` and `ImageData.resize`.

These calls are CPU-bound and run directly in the coroutine, so they block the event loop. While a large reprojection runs, every other request on that worker waits, and so do the in-flight `asyncio.gather` reads.

## Approach
- Run the blocking calls with `asyncio.to_thread`:
  - the project requires Python >= 3.12, so `to_thread` is always available;
  - `asyncer.asyncify` is a typed wrapper around `anyio.to_thread.run_sync`, which is only useful for trio support or anyio's thread limiter, and we need neither;
  - `rasterio.warp.reproject` releases the GIL during the GDAL warp, and numpy releases it for most array operations, so worker threads give real parallelism and not only a responsive loop.
- **GDAL environment**: rasterio stores the `Env` in a thread-local, and `to_thread` copies only contextvars. The helper wraps the function with the existing `rio_tiler.utils.inherit_rasterio_env`, which captures `rasterio.env.getenv()` in the caller and re-applies it in the worker thread, so options such as `GDAL_NUM_THREADS` or `CHECK_WITH_INVERT_PROJ` still apply.
- Offloading is unconditional. A thread hop costs ~50–100 µs, which is negligible next to a warp.

## Implementation

### 1. Helper: `rio_tiler.utils.run_sync`
It reuses the existing `inherit_rasterio_env`, which already copies the caller's rasterio env into another thread:
```python
async def run_sync(func: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R:
    return await asyncio.to_thread(inherit_rasterio_env(func), *args, **kwargs)
```
The first commit added it as `rio_tiler/experimental/_utils.py`. A later commit moved it to `rio_tiler/utils.py` and made it public. This is additive, not a breaking change.

### 2. `rio_tiler/experimental/geotiff.py` (`Reader`)
- `part()`: `img = await run_sync(warp, img, ...)`
- `preview()`: `await run_sync(img.reproject, ...)` and `await run_sync(img.resize, ...)`

### 3. `rio_tiler/experimental/zarr.py` (`AsyncArrayReader` only)
- The same three call sites as for the GeoTIFF reader.
- `AsyncGroupReader` gets the change through `AsyncArrayReader`.
- The sync `ArrayReader`/`GroupReader` are not changed.

### 4. `CHANGES.md`
- Add a `fix:` entry under Unreleased.

## Commits
1. `feat: add run_sync helper to offload blocking calls to a thread`
2. `feat(experimental): offload warp/reproject/resize to a thread in async GeoTIFF Reader`
3. `feat(experimental): offload warp/reproject/resize to a thread in zarr AsyncArrayReader`
4. `docs: update changelog`
5. `docs: add plan` (this file)
6. `refactor: move run_sync to rio_tiler.utils and reuse inherit_rasterio_env`

## Testing
- `tests/test_utils.py`:
  - `run_sync` runs in a different thread and passes args and kwargs;
  - no `rasterio.Env` in the caller means none in the worker;
  - options from `rasterio.Env(GDAL_NUM_THREADS="2")` are visible in the worker.
- Existing reader tests must pass unchanged (the outputs are the same):
  `pytest tests/test_async_geotiff.py tests/test_zarr_array.py tests/test_zarr_group.py`

## Out of scope / follow-ups
- `apply_expression` and `statistics` still run on the loop. They are usually cheap, but they can be wrapped the same way if profiling shows they matter.
- `rasterize` in `feature()` is also left on the loop.
- `rio_tiler.experimental.xarray.GeoArrayReader` is synchronous, so it needs no change.
- Thread pool sizing: the default executor has `min(32, cpu + 4)` threads. If `GDAL_NUM_THREADS` is also set, the total can oversubscribe the CPU. Document this, or let users pass an executor, only if it shows up in practice.
