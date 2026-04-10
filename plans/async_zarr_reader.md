# Plan: AsyncZarrReader Implementation

## TL;DR
Build a minimal pure zarr-python async reader in rio-tiler that accepts a zarr `AsyncArray` plus geospatial metadata (bounds, transform, crs) as input. First version implements only `part()` method with flexible 2D/3D array support and nodata handling via options + fallback to fill_value.

## Steps

### Phase 1: Core Infrastructure

1. **Update `AsyncZarrReader` class definition** ([_async.py](rio_tiler/experimental/_async.py#L873-L896))
   - Change `input: AsyncArrayV3` to accept `zarr.core.array.AsyncArray` (the proper generic type)
   - Add `nodata` to `ZarrOptions` type (already there, ensure it's used)
   - Make `height` and `width` init-able from attrs (not from zarr shape directly)
   - Remove `_dims` private attribute (not needed for minimal version)

2. **Implement `__attrs_post_init__`** — derive width/height from input array shape
   - Check array.shape for 2D `(height, width)` or 3D `(bands, height, width)`
   - Set `self.height` and `self.width` from shape
   - Derive nodata: `options.get("nodata") or getattr(self.input, "fill_value", None)`

### Phase 2: Core Read Method

3. **Implement `_read()` method** — async read from zarr array with selection
   - Accept `selection: tuple[slice, ...] | None` for pixel window
   - Use `await self.input.getitem(selection)` for async read (zarr v3 API)
   - Handle 2D→3D promotion: if array is 2D, add band axis
   - Apply index selection for band filtering
   - Create nodata mask from fill_value/nodata option
   - Return `ImageData` with proper bounds from selection + transform

### Phase 3: Part Method

4. **Implement `part()` method** — read bbox as ImageData (*minimal first version*)
   - Convert bbox to pixel window using `rasterio.windows.from_bounds()`
   - Handle CRS reprojection: transform bbox if `bounds_crs != self.crs`
   - Calculate output dimensions from bbox and resolution (or use explicit width/height)
   - Clamp window to array bounds
   - Call `_read()` with pixel selection
   - Use `warp()` helper for reprojection/resampling if dst_crs differs

### Phase 4: Tile (inherits from part)

5. **Implement `tile()` method** — delegates to `part()` with tile bounds
   - Use TMS to calculate tile bbox
   - Call `part()` with proper dimensions (256/512 based on tilesize)

## Relevant Files

- [rio_tiler/experimental/_async.py](rio_tiler/experimental/_async.py#L867-L1030) — `AsyncZarrReader` class and `ZarrOptions`, `warp()` helper
- [rio_tiler/io/base.py](rio_tiler/io/base.py) — `SpatialMixin` with minzoom/maxzoom and `tile_exists()`
- [rio_tiler/models.py](rio_tiler/models.py) — `ImageData` and `PointData` constructors
- [rio_tiler/utils.py](rio_tiler/utils.py) — `_get_width_height`, `_missing_size`, `cast_to_sequence`

## Verification

1. **Unit test `_read()`**: Create in-memory zarr array, call `_read()`, verify ImageData shape and nodata mask
2. **Unit test `part()`**: Create georeferenced zarr array, read bbox subset, verify bounds and data
3. **Unit test 2D vs 3D**: Ensure both `(100, 100)` and `(3, 100, 100)` shaped arrays work
4. **Integration test**: Use existing zarr test fixture (if available) or create minimal zarr store

## Decisions

- **Import**: Use `zarr.core.array.AsyncArray` generic type (works for v2/v3)
- **Array shape**: Support both 2D and 3D, promoting 2D to 3D with single band
- **Nodata**: Prefer `options["nodata"]`, fallback to `input.fill_value`
- **Scope**: Part only for v1 — tile/preview/point/feature/info/statistics in future iterations
- **No multiscale**: First version assumes single-resolution array (no overview selection logic)

## Further Considerations

1. **Band dimension position**: Assume bands-first (C, H, W). Should we detect or allow configuration? *Recommend*: Assume bands-first for consistency with rasterio, document requirement.

2. **Async getitem vs orthogonal_selection**: zarr v3 `AsyncArray` supports `getitem()` directly, but `get_orthogonal_selection()` may be needed for advanced slicing. *Recommend*: Start with `getitem()`, switch if needed.

## Status: ✅ Implemented

The following methods are now working:
- `_read()` — async read with windowed slices, handles 2D/3D arrays
- `part()` — bbox-based reads with CRS transformation and reprojection
- `tile()` — delegates to `part()` with TMS tile bounds

**Not yet implemented** (raise `NotImplementedError`):
- `info()`, `statistics()`, `preview()`, `point()`, `feature()`
