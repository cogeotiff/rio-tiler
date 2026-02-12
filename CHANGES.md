
# Unreleased

# 9.0.0a4 (2026-02-11)

* fix: type hint for ImageData/PointData methods
* remove: `typing-extensions` from requirements

# 9.0.0a3 (2026-02-05)

* add: `inherit_rasterio_env` decorator to `utils` module for decorating functions that need to inherit rasterio env settings from a parent thread.
* fix: automatically forward rasterio env settings to threads in multibase reader

# 9.0.0a2 (2026-02-04)

* change: `MultiReaderBase._get_reader` signature to only return `type[BaseReader]`
* add: `reader_options` in `AssetInfo` model

# 9.0.0a1 (2026-02-03)

* remove: default tilesize option (`256`) for `tile()` methods and default to TMS tilematrix `tileHeight` and `tileWidth`
* remove: `parse_expression` method in `MultiBaseReader`
* remove: `asset_indexes` option for `MultiBaseReader`
* change: band indexes in `ImageData.band_names` for Reader's responses

    ```python
    # before
    with Reader(path) as src:
        img = src.read(indexes=(1,1,))
        print(img.band_names)
        >> ["b1", "b1"]

    # now
    with Reader(path) as src:
        img = src.read(indexes=(1,1,))
        print(img.band_names)
        >> ["b1", "b2"]
    ```

* change: deprecate `MultiBandReader`
* change: type informations for `AssetInfo` model

    ```python
    class AssetInfo(TypedDict):
        """Asset Reader Options."""

        url: Any
        name: str
        media_type: str | None
        method_options: dict
        env: NotRequired[dict]
        metadata: NotRequired[dict]
        dataset_statistics: NotRequired[Sequence[tuple[float, float]]]
    ```

* change: in `MultiBaseReader`, expression are now in form of `b1/b2` indicating the band index within the ImageData object returned by the `read` method

    ```python
    with MultiBaseReader(input) as src:
        # asset1 and asset2 are both 1-band dataset
        src.preview(assets=["asset1", "asset2"], expression="b1+b2")

        # asset1 has 1 band while asset3 has 2 bands
        src.preview(assets=["asset1", "asset3"], expression="b1+b2/b3")
    ```

* change: STACReader now accept `assets` options in form of `assets="{asset_name}|some_option=some_value&another_option=another_value"` (e.g `assets=visual|indexes=1,2,3`). Asset's parsing is done in `_get_asset_info` method.
* change: use band name (index) instead of band's description in statistics

    ```python
    # before
    with Reader(path) as src:
        img = src.read()
        print(img.band_names)
        >> ["b1", "b2", "b3"]
        >> ["red", "green", "blue"]  # or ["", "", ""] if no band description

        stats = src.statistics(expression="b1+2")
        print(list(stats))
        >> "b1+2"

    # now
    with Reader(path) as src:
        img = src.read()
        print(img.band_names)
        >> ["b1", "b2", "b3"]
        >> ["red", "green", "blue"]  # or ["b1", "b2", "b3"] if no band description

        stats = src.statistics(expression="b1+2")
        print(list(stats))
        >> "b1"
        print(stats["b1"].description)
        >> "red+2"  # b1+2 if no band description
    ```

* add: `method_options` attribute in `AssetInfo`. Used in `MultiBaseReader` to pass method's options
* add: `description` in `BandStatistics` model
* add: infer band description in `ImageData.apply_expression()` result's band_descriptions

    ```python
    # before
    with Reader(COG_TAGS) as src:
        img = src.preview(expression="b1*2")
        assert img.band_descriptions == [""]

    # now
    with Reader(COG_TAGS) as src:
        img = src.preview(expression="b1*2")
        assert img.band_descriptions == ["Green*2"]
    ```

# 8.0.5 (2026-01-05)

* improve type hints - part 2: change old Union and `typing.*` notations

# 8.0.4 (2015-12-15)

* add support for python 3.14

# 8.0.3 (2015-12-15)

* improve and fix type hints

# 8.0.2 (2025-12-04)

* add arguments to `rio_tiler.mosaic.BaseBackend`'s `statistics` and `preview` methods to avoid `unexpected keyword argument` errors

# 8.0.1 (2025-11-21)

* Better handle mask and alpha band from colormap when rendering images

# 8.0.0 (2025-11-20)

* remove python 3.9 and 3.10 support **breaking change**

* add **band_descriptions** in ImageData and PointData objects

```python
with Reader("tests/fixtures/cog_tags.tif") as src:
    info = src.info()
    img = src.preview()

    print(info.band_descriptions)
    >> [('b1', 'Green')]

    print(img.band_names)
    >> ['b1']

    print(img.band_descriptions)
    >> ['Green']
```

* use `b{idx}` as band names in `XarrayReader` result (instead of band descriptions) **breaking change**

```python
    arr = numpy.arange(0.0, 33 * 35 * 2, dtype="float32").reshape(2, 33, 35)
    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": numpy.arange(-170, 180, 10),
            "y": numpy.arange(-80, 85, 5),
            "time": [datetime(2022, 1, 1), datetime(2022, 1, 2)],
        },
    )
    data.attrs.update({"valid_min": arr.min(), "valid_max": arr.max()})
    data.rio.write_crs("epsg:4326", inplace=True)

    # Before
    with XarrayReader(data) as dst:
        assert info.band_metadata == [("b1", {}), ("b2", {})]
        assert info.band_descriptions == [
            ("b1", "2022-01-01T00:00:00.000000000"),
            ("b2", "2022-01-02T00:00:00.000000000"),
        ]

        stats = dst.statistics()
        assert list(stats) == [
            "2022-01-01T00:00:00.000000000",
            "2022-01-02T00:00:00.000000000",
        ]

        img = dst.tile(0, 0, 0)
        assert img.band_names == [
            "2022-01-01T00:00:00.000000000",
            "2022-01-02T00:00:00.000000000",
        ]

    # Now
    with XarrayReader(data) as dst:
        stats = dst.statistics()
        assert list(stats) == [
            "b1",
            "b2",
        ]

        img = dst.tile(0, 0, 0)
        assert img.band_names == [
            "b1",
            "b2",
        ]
        assert img.band_descriptions == [
            "2022-01-01T00:00:00.000000000",
            "2022-01-02T00:00:00.000000000",
        ]
```

* rename `XarrayReader.band_names` -> `XarrayReader.band_descriptions`  **breaking change**

* only cast data to `uint8` if colormap values are of type `uint8`

* add `alpha_mask` attribute to `ImageData` class

* allow partial alpha values from alpha band

* better handle non-uint8 alpha band

* remove deprecated `force_binary_mask` option in `reader.read` function  **breaking change**

* add `nodata`, `scales` and `offsets` attributes to `ImageData` and `PointData` classes

* add `rio_tiler.experimental.zarr.ZarrReader` Zarr Dataset experimental reader

* refactor `XarrayReader.part` method to better handle reprojection and re-usability
* move `_get_width_height` and `_missing_size` from `rio_tiler.reader` to `rio_tiler.utils`
* add upper memory limit for Xarray dataset. Controled with `RIO_TILER_MAX_ARRAY_SIZE` env variable.
* add Mosaic Backend abstract base class
* update morecantile requirements to `>=5.0,<8.0`

# 7.9.3 (2026-02-12)

* add upper memory limit for Xarray dataset. Controled with `RIO_TILER_MAX_ARRAY_SIZE` env variable  **Backported**

# 7.9.2 (2025-10-09)

* fix: bad code logic in XarrayReader

# 7.9.1 (2025-10-09)

* fix: better handler inverted (SouthUp) dataset in XarrayReader

# 7.9.0 (2025-10-07)

* refactor XarrayReader.part method to better handle reprojection and re-usability (<https://github.com/cogeotiff/rio-tiler/pull/828>) **Backported**
* move `_get_width_height` and `_missing_size` from `rio_tiler.reader` to `rio_tiler.utils` **Backported**

# 7.8.1 (2025-06-16)

* apply scale/offset to dataset statistics in ImageData object (used for automatic rescaling)

# 7.8.0 (2025-06-03)

* add `to_raster()` method to `ImageData` class

# 7.7.4 (2025-05-29)

* fix band names for Xarray DataArray

# 7.7.3.post1 (2025-05-22)

* remove unwanted breaking change

# 7.7.3 (2025-05-22) **YANKED**

* fix Boundless `part` read when using GCPs dataset

# 7.7.2 (2025-05-15)

* add `repr` method to Mosaic Method classes
* add metadata (pixel selection method, assets count, asset used count) on Image/Point object returned by `mosaic_reader`

    ```python
    from rio_tiler.io import Reader
    from rio_tiler.mosaic import mosaic_reader

    def tiler(src_path: str, *args, **kwargs):
        with Reader(src_path) as src:
            return src.tile(*args, **kwargs)

    mosaic_assets = ["tests/fixtures/mosaic_value_1.tif", "tests/fixtures/mosaic_value_1.tif", "tests/fixtures/mosaic_value_2.tif"]
    x = 150
    y = 182
    z = 9

    # Use Default First value method
    img, _ = mosaic_reader(mosaic_assets, tiler, x, y, z)
    print(img.metadata)
    >> {'mosaic_method': 'FirstMethod', 'mosaic_assets_count': 3, 'mosaic_assets_used': 1}
    ```

# 7.7.1 (2025-05-13)

* add `max`, `min`, `med`, `q1` and `q3` resampling methods to `WarpResampling` literal

# 7.7.0 (2025-05-05)

* fix size estimation when using `window` an `reader.read` method
* add `width` or `height` estimation when passing only one size

# 7.6.1 (2025-04-22)

* fix Xarray indexes check when passing a list

# 7.6.0 (2025-03-31)

* add `interpolate=True/False` to `.point()` methods to allow interpolation of surrounding pixels

    ```python
    with Reader("tests/fixtures/cog.tif") as src:
        pt = src.point(-57.566, 73.68856)
        print(pt.data[0])
        >> 2800

        pt = src.point(-57.566, 73.68856, interpolate=True, resampling_method="bilinear")
        print(pt.data[0])
        >> 2819
    ```

* add `pixel_location` property to `PointData` model

    ```python
    with Reader("tests/fixtures/cog.tif") as src:
        pt = src.point(-57.566, 73.68856)
        print(pt.pixel_location)
        >> (1090, 1086)

    with Reader("tests/fixtures/cog.tif") as src:
        pt = src.point(-57.566, 73.68856, interpolate=True)
        print(pt.pixel_location)
        >> (1090.5924744641266, 1086.2541429827688)
    ```

* add `out_dtype` to reader's methods to allow user setting the output data type

    ```python
    from rio_tiler.io import Reader

    with Reader("tests/fixtures/cog.tif") as src:
        img = src.preview()
        print(img.array.dtype)
        >> uint16

        img = src.preview(out_dtype="float32")
        print(img.array.dtype)
        >> float32
    ```

* update pystac dependency to `>=1.9,<2.0`

# 7.5.1 (2025-03-19)

* fix `utils.get_array_statistics` method to avoid `ZeroDivisionError` when there is no valid pixel
* use `GDAL_MEM_ENABLE_OPEN=TRUE` when opening a numpy array with rasterio

# 7.5.0 (2025-02-26)

* add `rio_tiler.experimental` submodule
* add `rio_tiler.experimental.vsifile.VSIReader` VSIFile based experimental reader

# 7.4.0 (2025-01-28)

* update rasterio dependency to `>=1.4.0`

* add `reproject` method for `ImageData` objects (author @emmanuelmathot, <https://github.com/cogeotiff/rio-tiler/pull/782>)

    ```python
    from rio_tiler.models import ImageData

    img = ImageData(numpy.zeros((3, 256, 256), crs=CRS.from_epsg(4326), dtype="uint8"))
    img_3857 = img.reproject("epsg:3857")
    ```

* add `indexes` parameter for `XarrayReader` methods. As for Rasterio, the indexes values start at `1`.

    ```python
    data = ... # DataArray of shape (2, x, y)

    # before
    with XarrayReader(data) as dst:
        img = dst.tile(0, 0, 0)
        assert img.count == 2

    # now
    with XarrayReader(data) as dst:
        # Select the first `band` within the data array
        img = dst.tile(0, 0, 0, indexes=1)
        assert img.count == 1
    ```

* better define `band names` for `XarrayReader` objects

  * band_name for `2D` dataset is extracted form the first `non-geo` coordinates value

        ```python
        data = xarray.DataArray(
            numpy.arange(0.0, 33 * 35 * 2).reshape(2, 33, 35),
            dims=("time", "y", "x"),
            coords={
                "x": numpy.arange(-170, 180, 10),
                "y": numpy.arange(-80, 85, 5),
                "time": [datetime(2022, 1, 1), datetime(2022, 1, 2)],
            },
        )
        da = data[0]

        print(da.coords["time"].data)
        >> array('2022-01-01T00:00:00.000000000', dtype='datetime64[ns]'))

        # before
        with XarrayReader(data) as dst:
            img = dst.info()
            print(img.band_descriptions)[0]
            >> ("b1", "value")

        # now
        with XarrayReader(data) as dst:
            img = dst.info()
            print(img.band_descriptions)[0]
            >> ("b1", "2022-01-01T00:00:00.000000000")
        ```

  * default `band_names` is changed to DataArray's name or `array` (when no available coordinates value)

        ```python
        data = ... # DataArray of shape (x, y)

        # before
        with XarrayReader(data) as dst:
            img = dst.info()
            print(img.band_descriptions)[0]
            >> ("b1", "value")

        # now
        with XarrayReader(data) as dst:
            img = dst.info()
            print(img.band_descriptions)[0]
            >> ("b1", "array")
        ```

# 7.3.1 (2025-01-23)

* make sure `STACReader.transform` is an Affine object

# 7.3.0 (2025-01-07)

* drop python 3.8 support
* add python 3.13 support
* fix: use coverage array for calculation of valid_percent (author @MarcelCode, <https://github.com/cogeotiff/rio-tiler/pull/775>)

# 7.2.2 (2024-11-18)

* Catch and expand error message when GDAL cannot encode data using specified image driver (<https://github.com/cogeotiff/rio-tiler/pull/767>)

# 7.2.1 (2024-11-14)

* add official support for floating point values in ColorMap
* cast data to `uint8` datatype when applying linear colormap

# 7.2.0 (2024-11-05)

* Ensure compatibility between XarrayReader and other Readers by adding `**kwargs` on class methods (<https://github.com/cogeotiff/rio-tiler/pull/762>)

* add `STACReader.get_asset_list()` method to enable easier customization of the asset listing/validation (<https://github.com/cogeotiff/rio-tiler/pull/762>)

# 7.1.0 (2024-10-29)

* Add `preview()` and `statistics()` methods to XarrayReader (<https://github.com/cogeotiff/rio-tiler/pull/755>)

* Add output size (`max_size` | `width`, `height`) options for XarrayReader's `preview()`, `part()` and `feature()` methods (<https://github.com/cogeotiff/rio-tiler/pull/755>)

* Add half X/Y resolution on bounds before checking the geographic bounds in XarrayReader (<https://github.com/cogeotiff/rio-tiler/pull/755>)

* Check if the Y bounds are inverted and flip the image on the Y axis in XarrayReader (<https://github.com/cogeotiff/rio-tiler/pull/756>)

* Add support for 2D arrays in XarrayReader (<https://github.com/cogeotiff/rio-tiler/pull/755>)

* Cast Xarray `attrs` values in XarrayReader's `info()` response to avoid JSON encoding issues (<https://github.com/cogeotiff/rio-tiler/pull/755>)

* Refactor XarrayReader's `feature()` method to use the `part` method (<https://github.com/cogeotiff/rio-tiler/pull/755>)

* Allow `op` parameter for `create_cutline` and `_convert_to_raster_space` functions to better control rasterio's `rowcol` behaviour (author @Martenz, <https://github.com/cogeotiff/rio-tiler/pull/759>)

# 7.0.1 (2024-10-22)

* Add `CRS_to_urn` method and update internals for `CRS_to_uri` (author @AndrewAnnex, <https://github.com/cogeotiff/rio-tiler/pull/752>)

# 7.0.0 (2024-10-21)

* Enable dynamic definition of Asset **reader** in `MultiBaseReader` (<https://github.com/cogeotiff/rio-tiler/pull/711/>, <https://github.com/cogeotiff/rio-tiler/pull/728>)

* Adding `default_assets` for MultiBaseReader and STACReader (author @mccarthyryanc, <https://github.com/cogeotiff/rio-tiler/pull/722>)

* Adding `default_bands` for MultiBandReader (<https://github.com/cogeotiff/rio-tiler/pull/722>)

* Adding support for the STAC `Projection` extension to derive the `bounds`, `crs`, `minzoom` and `maxzoom` properties  **breaking change**

* Refactor internal function and base classes for the `minzoom/maxzoom` calculation **breaking change**

* Adding `transform`, `height` and `width` attributes (outside init) for `SpatialMixin` class

* Moved `_dst_geom_in_tms_crs` from Reader to `SpatialMixin` class **breaking change**

* Removed use of rasterio's `is_tiled` method

* Enable **Alternate** asset's HREF for STAC by using `RIO_TILER_STAC_ALTERNATE_KEY` environment variable

* Adding support for GDAL VRT Connection string for STAC Assets

* Improve type hint definition

* make `ImageData.rescale` and `ImageData.apply_color_formula` to return `self`

* add support for `.json` colormap files

* do no `lowercase` colormap name in `ColorMaps.get` method **breaking change**

    ```python
    from rio_tiler.colormap import cmap

    # before
    assert cmap.get("Viridis")

    # now
    assert cmap.get("Viridis")
    >> InvalidColorMapName: Invalid colormap name: Viridis
    ```

* removed `geographic_crs` attribute in `SpatialMixin` class **breaking change**

* removed `geographic_bounds` property in `SpatialMixin` class **breaking change**

* add `get_geographic_bounds(crs: CRS)` method in `SpatialMixin` class

    ```python
    from rasterio.crs import CRS
    from rio_tiler.io import Reader

    # before
    with Reader("cog.tif", geographic_crs=CRS.from_epsg(4326)) as src:
        bounds = src.geographic_bounds

    # now
    with Reader("cog.tif") as src:
        bounds = src.get_geographic_bounds(CRS.from_epsg(4326))
    ```

* replace `geographic bounds` with dataset bounds in `Reader.info()` method's response **breaking change**

    ```python
    from rio_tiler.io import Reader

    # before
    with Reader("cog.tif") as src:
        assert src.geographic_bounds == src.info().bounds

    # now
    with Reader("cog.tif") as src:
        assert src.bounds == src.info().bounds
    ```

* add `crs: str` property in `Info` model

* remove `minzoom` and `maxzoom` properties in `Info` model **breaking change**

* update `morecantile` dependency to allow `6.x` version

* remove deprecated method and attributes

* `round` xarray dataset's bounds to avoid precision errors when checking for valid geographic bounding box

* fix `bounds` type information

# 6.8.0 (2024-10-23)

* Enable **Alternate** asset's HREF for STAC by using `RIO_TILER_STAC_ALTERNATE_KEY` environment variable [Backported from `7.0`]

* Adding support for GDAL VRT Connection string for STAC Assets [Backported from `7.0`]

# 6.7.0 (2024-09-05)

* raise `MissingCRS` or `InvalidGeographicBounds` errors when Xarray datasets have wrong geographic metadata
* better error message for `TileOutsideBounds` errors (author @abarciauskas-bgse, <https://github.com/cogeotiff/rio-tiler/pull/712>)
* handle of inverted latitude in `reader.point` (author @georgespill, <https://github.com/cogeotiff/rio-tiler/pull/716>)

# 6.6.1 (2024-05-17)

* fix/support `scale/offset` indexes selection (author @jddeal, <https://github.com/cogeotiff/rio-tiler/pull/709>)

# 6.6.0 (2024-05-16)

* fix type hint for `ImageData.band_names` (author @n8sty, <https://github.com/cogeotiff/rio-tiler/pull/704>)
* enable `per-band` scale/offset rescaling (co-author @jddeal, <https://github.com/cogeotiff/rio-tiler/pull/707>)
* replace `scale` and `offset` by `scales` and `offsets` in `rio_tiler.models.Info` model

    ```python
    # before
    with Reader("tests/fixtures/cog_scale.tif") as src:
        info = src.info()
        print(info.scale, info.offset)
    >> 0.0001 1000.0

    # now
    with Reader("tests/fixtures/cog_scale.tif") as src:
        info = src.info()
        print(info.scales, info.offsets)
    >> [0.0001, 0.001] [1000.0, 2000.0]
    ```

# 6.5.0 (2024-05-03)

* Revert [#648](https://github.com/cogeotiff/rio-tiler/pull/648) and refactor `get_vrt_transform` method to better handle over-zooming a dataset

# 6.4.7 (2024-04-17)

* Better handle dataset with inverted origin
* make sure datatype is forwarded to the WarpedVRT

# 6.4.6 (2024-04-09)

* Ignore STAC statistics object when they contain invalid type (author @emmanuelmathot, <https://github.com/cogeotiff/rio-tiler/pull/695>)

# 6.4.5 (2024-04-05)

* add python 3.12 official support
* change code formatter to `ruff-format`

# 6.4.4 (2024-04-02)

* better handler `NaN` nodata values for masking (author @cerolinx, <https://github.com/cogeotiff/rio-tiler/pull/691>)

# 6.4.3 (2024-03-22)

* make sure `scale` and `offset` are set in `Info` even when `offset=0.` or `scale=1.0` (<https://github.com/cogeotiff/rio-tiler/pull/687>)

# 6.4.2 (2024-03-22)

* better account for coverage in statistics (<https://github.com/cogeotiff/rio-tiler/pull/684>)

# 6.4.1 (2024-02-19)

* add `CountMethod` mosaic method (author @mccarthyryanc, <https://github.com/cogeotiff/rio-tiler/pull/676>)

# 6.4.0 (2024-01-24)

* deprecate `resampling_method` in `rio_tiler.io.xarray.XarrayReader` method and add `reproject_method` (to match the `rio_tiler.io.Reader` options)

    ```python
    # before
    with XarrayReader(data) as dst:
        img = dst.tile(0, 0, 1, resampling_method="cubic")

    # now
    with XarrayReader(data) as dst:
        img_cubic = dst.tile(0, 0, 1, reproject_method="cubic")
    ```

# 6.3.1 (2024-01-22)

* When overriding **nodata**, do not mix mask and only use the provided nodata value

# 6.3.0 (2024-01-16)

* do not use `warpedVRT` when overwriting the dataset nodata value

* add `align_bounds_with_dataset` option in `rio_tiler.reader.part` to align input bounds with the dataset resolution

    <img src="https://github.com/cogeotiff/rio-tiler/assets/10407788/0e340d3d-e5d9-4558-93f7-3f307c017510" style="max-width: 500px;">

# 6.2.10 (2024-01-08)

* remove default Endpoint URL in AWS S3 Client for STAC Reader

# 6.2.9 (2023-12-21)

* fix AWS endpoint credential for STAC `fetch` function, using same defaults as GDAL vsis3 configuration

# 6.2.8 (2023-12-11)

* apply `discrete` colormap when the provided colormap does not have 256 values

# 6.2.7 (2023-11-29)

* Adjusting dataset latitude for WarpedVRT parameters calculation when EPSG:4326 dataset latitudes overflows EPSG:3857 min/max latitude (<https://github.com/cogeotiff/rio-tiler/pull/660>)

# 6.2.6 (2023-11-10)

* validate `shape` in `ImageData.get_coverage_array` to avoid rasterio error when re-projecting the geometry

# 6.2.5 (2023-11-06)

* avoid `indexes` collision in `MultiBaseReader`

# 6.2.4 (2023-10-19)

* fix issue with `WarpedVRT` when doing re-projection (ref: <https://github.com/cogeotiff/rio-tiler/pull/648>)

* move benchmark outside pytest suite

* add GET/HEAD request tests using tilebench (outside pytest suite) (ref: <https://github.com/cogeotiff/rio-tiler/pull/649>)

# 6.2.3.post1 (2023-11-16)

* validate `shape` in `ImageData.get_coverage_array` to avoid rasterio error when re-projecting the geometry [Backported from 6.2.6]
* avoid `indexes` collision in `MultiBaseReader` [Backported from 6.2.5]

This release was made while we waited on a fix for <https://github.com/cogeotiff/rio-tiler/issues/654>

# 6.2.3 (2023-10-11)

* in `STACReader` use `href` if `get_absolute_href()` returns `None`

# 6.2.2 (2023-10-05)

* add list of assets in `InvalidAssetName` message in `STACReader`

# 6.2.1 (2023-09-28)

* allow GeoJSON `Feature` in `ImageData.get_coverage_array` method

# 6.2.0 (2023-09-27)

* allow area-weighted statistics by adding `coverage` option in `rio_tiler.utils.get_array_statistics`

    ```python
    # Data Array
    # 1, 2
    # 3, 4
    data = numpy.ma.array((1, 2, 3, 4)).reshape((1, 2, 2))

    # Coverage Array
    # 0.5, 0
    # 1, 0.25
    coverage = numpy.array((0.5, 0, 1, 0.25)).reshape((2, 2))

    stats = utils.get_array_statistics(data, coverage=coverage)
    assert len(stats) == 1
    assert stats[0]["min"] == 1
    assert stats[0]["max"] == 4
    assert stats[0]["mean"] == 1.125  # (1 * 0.5 + 2 * 0.0 + 3 * 1.0 + 4 * 0.25) / 4
    assert stats[0]["count"] == 1.75  # (0.5 + 0 + 1 + 0.25) sum of the coverage array

    stats = utils.get_array_statistics(data)
    assert len(stats) == 1
    assert stats[0]["min"] == 1
    assert stats[0]["max"] == 4
    assert stats[0]["mean"] == 2.5
    assert stats[0]["count"] == 4
    ```

* add `rio_tiler.utils.get_coverage_array` method to create a `coverage %` array

* add `cmocean` colormaps

    <img src="https://raw.githubusercontent.com/cogeotiff/rio-tiler/main/docs/src/img/colormaps_for_oceanography.png" style="max-width: 500px;">

* allow uppercase in `cmap.get` method

    ```python
    from rio_tiler.colormap import cmap

    # Before
    cm = cmap.get("greys")

    # Now
    cm = cmap.get("Greys")
    ```

# 6.1.0 (2023-09-15)

* add `width`, `height` and `count` properties in `MosaicMethodBase`
* make sure we mosaic ImageData/PointData with same number of bands
* resize `ImageData.array` to the first asset's width/height in `mosaic_reader`

# 6.0.3 (2023-09-13)

* return a 1x1 image when bbox is smaller than a single pixel (author @JackDunnNZ, <https://github.com/cogeotiff/rio-tiler/pull/637>)

# 6.0.2 (2023-08-21)

* Update `data_as_image` to return masked values (author @JackDunnNZ, <https://github.com/cogeotiff/rio-tiler/pull/635>)

# 6.0.1 (2023-07-25)

* fix `key` access for `Info` and `BandStatistics` models for `extra` attributes
* update deprecation notice to `7.0`

# 6.0.0 (2023-07-25)

* update `morecantile` requirement to `>=5.0,<6.0`
* delete `rio_tiler.models.NodataTypes` (replaced with Literal within the `Info` model)

# 5.0.3 (2023-07-18)

* Filter useless `NotGeoreferencedWarning` warnings in  `Reader.feature()` and `ImageData.from_bytes()` methods
* Ensure that dataset is still open when reading tags (author @JackDunnNZ, <https://github.com/cogeotiff/rio-tiler/pull/628>)

# 5.0.2 (2023-07-11)

* fix `ImageData.apply_color_formula()` method

# 5.0.1 (2023-06-22)

* raise `InvalidExpression` when passing invalid `asset` or `band` in an expression

# 5.0.0 (2023-06-01)

* Fix potential issue when getting statistics for non-valid data

* add `rio-tiler.mosaic.methods.PixelSelectionMethod` enums with all defaults methods

* Add `rio-tiler.utils._validate_shape_input` function to check geojson feature inputs

* Change cutline handling in the `rio-tiler.io.rasterio.Reader.feature` method. Feature
  cutlines are now rasterized into numpy arrays and applied as masks instead of using
  the cutline vrt_option. These masks are tracked in the `rio-tiler.models.ImageData.cutline_mask`
  attribute, which are used in `rio-tiler.mosaic.methods.base.MosaicMethodBase` to stop
  mosaic building as soon as all pixels in a feature are populated

* Fix missing `nodata/alpha/mask` forwarding for dataset with internal GCPS

* in `rio_tiler.io.XarrayReader`, add `auto_expand` options to avoid returning 1D array (incompatible with rio-tiler) (author @abarciauskas-bgse, <https://github.com/cogeotiff/rio-tiler/pull/608>)

* handle internal and user provided `nodata` values in `rio_tiler.io.XarrayReader` to create mask

* add `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `AWS_PROFILE` and `AWS_REGION` environnement overrides for `rio_tiler.io.stac.aws_get_object` function

**breaking changes**

* remove support for non-binary mask values (e.g non-binary alpha bands, ref: [rasterio/rasterio#1721](https://github.com/rasterio/rasterio/issues/1721#issuecomment-586547617))

* switch from PER-DATASET to PER-BAND mask (<https://github.com/cogeotiff/rio-tiler/pull/580>)

    ```python
    # before
    with COGReader("cog.tif") as src:
        img = src.preview(width=128, height=128, max_size=None)
        assert img.data.shape == (3, 128, 128)
        assert img.mask.shape == (128, 128)

    # now
    with COGReader("cog.tif") as src:
        img = src.preview(width=128, height=128, max_size=None)
        assert isinstance(img.array, numpy.ma.MaskedArray)
        assert img.array.data.shape == (3, 128, 128)
        assert img.array.mask.shape == (3, 128, 128))
    ```

* use numpy masked array in ImageData and PointData to store the data

    ```python
    # before
    arr = numpy.zeros((1, 256, 256), dtype="uint16")
    img = ImageData(arr)
    assert isintance(img.data, numpy.ndarray)  # Attribute

    # now
    arr = numpy.zeros((1, 256, 256), dtype="uint16")
    img = ImageData(arr)
    assert isintance(img.array, numpy.ma.MaskedArray)  # Attribute
    assert isintance(img.data, numpy.ndarray)  # property
    assert isintance(img.mask, numpy.ndarray)  # property
    ```

* remove `ImageData.from_array` method (because we now support MaskedArray directly)

* `rio_tiler.expression.apply_expression` input/output type change to `numpy.ma.MaskedArray`

* rio-tiler `mosaic` methods return `numpy.ma.MaskedArray`

* reader's `post_process` should be a Callable with `numpy.ma.MaskedArray` input/output

* add `reproject_method` option in `rio_tiler.reader`'s method to select the `resampling` method used during reprojection

    ```python
    # before
    with Reader("cog.tif") as src:
        im = src.preview(
            dst_crs="epsg:4326",
            resampling_method="bilinear",  # use `bilinear` for both resizing and reprojection
        )

    # now
    with Reader("cog.tif") as src:
        im = src.preview(
            dst_crs="epsg:4326",
            resampling_method="cubic",  # use `cubic` for resizing
            reproject_method="bilinear",  # use `bilinear` for reprojection
        )
    ```

* refactored the `MosaicMethodBase` to use python's dataclass

* changed variable names in `MosaicMethodBase` (`tile` -> `mosaic`)

* `rio_tiler.mosaic.methods.defaults.LastBandHigh` renamed `LastBandHighMethod`

* `rio_tiler.mosaic.methods.defaults.LastBandLow` renamed `LastBandLowMethod`

* move `aws_get_object` from `rio_tiler.utils` to `rio_tiler.io.stac`

* make `boto3` an optional dependency (`python -m pip install rio-tiler["s3"]`)

* update `morecantile` dependency to `>=4.0`

* add `metadata` in ImageData/PointData from rasterio dataset `tags`

* forward statistics from the **raster STAC extension** to the ImageData object

    ```python
    with STACReader(STAC_RASTER_PATH) as stac:
        info = stac._get_asset_info("green")
        assert info["dataset_statistics"] == [(6883, 62785)]
        assert info["metadata"]
        assert "raster:bands" in info["metadata"]

        img = stac.preview(assets=("green", "red"))
        assert img.dataset_statistics == [(6883, 62785), (6101, 65035)]
        assert img.metadata["green"]  # extra_fields from the STAC assets (e.g `"raster:bands"`)
        assert img.metadata["red"]
    ```

* add Deprecation warning for `ImageData.from_array`, `ImageData.as_masked`, `PointData.as_masked` methods

# 4.1.13 (2023-06-22)

* raise InvalidExpression when passing invalid asset or band in an expression (Backported from 5.0.1)

# 4.1.12 (2023-06-16)

* fix issue with `rio_tiler.utils.get_array_statistics` when passing data with no `valid` value

# 4.1.11 (2023-05-18)

* in `rio_tiler.io.XarrayReader`, add `auto_expand` options to avoid returning 1D array (incompatible with rio-tiler) (author @abarciauskas-bgse, <https://github.com/cogeotiff/rio-tiler/pull/608>)

# 4.1.10 (2023-03-24)

* enable `boundless` geometry for cutline (author @yellowcap, <https://github.com/cogeotiff/rio-tiler/pull/586>)

# 4.1.9 (2023-02-28)

* Automatically expand 2D numpy array to 3D when creating ImageData

# 4.1.8 (2023-02-15)

* Fix dtype issue when working with Mosaics Methods. Mask should always been of type `Uint8`.
* Fix `ImageData.from_array` method when working with Masked array

# 4.1.7 (2023-02-07)

* add `from_array` and `from_bytes` ImageData creation methods
* add `statistics` method to ImageData

# 4.1.6 (2023-01-18)

* add `apply_colormap` method to the ImageData class
* fix potential datatype overflow when calculating the intersection of mask and alpha band when using Colormap

# 4.1.5 (2022-12-20)

* Fix inverted col/row check when doing window read of a non WarpedVRT dataset

# 4.1.4 (2022-12-16)

* add `rio_tiler.mosaic.mosaic_point_reader` function to create Point value from multiple observation

    ```python
    def reader(asset: str, *args, **kwargs) -> PointData:
        with Reader(asset) as src:
            return src.point(*args, **kwargs)

    pt: PointData = mosaic_point_reader(["cog.tif", "cog2.tif"], reader, 0, 0)
    ```

# 4.1.3 (2022-12-15)

* fix invalid definition of `PointData.mask` when mask is not provided. Makes sure it's a one element array.

# 4.1.2 (2022-12-15)

* raise `InvalidPointDataError` error when trying to create PointData from an empty list in `PointData.create_from_list`

# 4.1.1 (2022-12-12)

* fix invalid coordinates slicing for `XArrayReader.point()` method (author @benjaminleighton, <https://github.com/cogeotiff/rio-tiler/pull/559>)

# 4.1.0 (2022-11-24)

* add `asset_as_band` option in `MultiBaseReader` tile, part, preview, feature and point methods

```python
with STACReader(STAC_PATH) as stac:
    img = stac.tile(71, 102, 8, assets="green")
    assert img.band_names == ["green_b1"]

with STACReader(STAC_PATH) as stac:
    img = stac.tile(71, 102, 8, assets="green", asset_as_band=True)
    assert img.band_names == ["green"]

# For expression, without `asset_as_band` tag, users have to pass `_b{n}` suffix to indicate the band index
with STACReader(STAC_PATH) as stac:
    img = stac.tile(71, 102, 8, expression="green_b1/red_b1")
    assert img.band_names == ["green_b1/red_b1"]

with STACReader(STAC_PATH) as stac:
    img = stac.tile(71, 102, 8, expression="green/red", asset_as_band=True)
    assert img.band_names == ["green/red"]
```

# 4.0.0 (2022-11-21)

* remove deprecated code
  * `asset_expression` in MultiBaseReader
  * `GCPCOGReader`

# 4.0.0a2 (2022-11-15)

* use of `file:header_size` extension in `STACReader` to set `GDAL_INGESTED_BYTES_AT_OPEN` environment variable

**breaking changes**

* renamed `MultiBaseReader._get_asset_url` to `MultiBaseReader._get_asset_info` and change the output to return a dictionary in form of `{"url": ..., "env": ...}`

# 4.0.0a1 (2022-11-10)

* assign ColorInterp.alpha to rendered image when we add the mask band
* add `.clip(bbox: BBox)` and `.resize(height: int, width: int)` methods to ImageData object
* add python 3.11 support
* replace `rio-color` by `color-operations` module

# 4.0.0a0 (2022-10-20)

* add python 3.10 support
* add `apply_expression` method in `rio_tiler.models.ImageData` class
* update `rio-tiler.reader.read/part` to avoid using WarpedVRT when no *reprojection* or *nodata override* is needed
* add `rio_tiler.io.rasterio.ImageReader` to work either with Non-geo or Geo images in a Non-geo manner (a.k.a: in the pixel coordinates system)

    ```python
    with ImageReader("image.jpg") as src:
        im = src.part((0, 100, 100, 0))

    with ImageReader("image.jpg") as src:
        im = src.tile(0, 0, src.maxzoom)
        print(im.bounds)

    >>> BoundingBox(left=0.0, bottom=256.0, right=256.0, top=0.0)
    ```

* add `rio_tiler.io.xarray.XarrayReader` to work with `xarray.DataArray`

    ```python
    import xarray
    from rio_tiler.io import XarrayReader

    with xarray.open_dataset(
        "https://ncsa.osn.xsede.org/Pangeo/pangeo-forge/noaa-coastwatch-geopolar-sst-feedstock/noaa-coastwatch-geopolar-sst.zarr",
        engine="zarr",
        decode_coords="all"
    ) as src:
        ds = src["analysed_sst"][:1]
        ds.rio.write_crs("epsg:4326", inplace=True)

        with XarrayReader(ds) as dst:
            img = dst.tile(1, 1, 2)
    ```

    note: `xarray` and `rioxarray` optional dependencies are needed for the reader

**breaking changes**

* remove python 3.7 support
* update rasterio requirement to `>=1.3` to allow python 3.10 support
* rename `rio_tiler.io.cogeo` to `rio_tiler.io.rasterio`
* rename `COGReader` to `Reader`. We added `rio_tiler.io.COGReader` alias to `rio_tiler.io.Reader` backwards compatibility

    ```python
    # before
    from rio_tiler.io import COGReader
    from rio_tiler.io.cogeo import COGReader

    # now
    from rio_tiler.io import Reader
    from rio_tiler.io.rasterio import Reader
    ```

* `rio_tiler.readers.read()`, `rio_tiler.readers.part()`, `rio_tiler.readers.preview()` now return a ImageData object
* remove `minzoom` and `maxzoom` attribute in `rio_tiler.io.SpatialMixin` base class
* remove `minzoom` and `maxzoom` attribute in `rio_tiler.io.Reader` (now defined as properties)
* use `b` prefix for band names in `rio_tiler.models.ImageData` class (and in rio-tiler's readers)

    ```python
    # before
    with COGReader("cog.tif") as cog:
        img = cog.read()
        print(cog.band_names)
        >>> ["1", "2", "3"]

        print(cog.info().band_metadata)
        >>> [("1", {}), ("2", {}), ("3", {})]

        print(cog.info().band_descriptions)
        >>> [("1", ""), ("2", ""), ("3", "")]

        print(list(cog.statistics()))
        >>> ["1", "2", "3"]

    # now
    with Reader("cog.tif") as cog:
        img = cog.read()
        print(img.band_names)
        >>> ["b1", "b2", "b3"]

        print(cog.info().band_metadata)
        >>> [("b1", {}), ("b2", {}), ("b3", {})]

        print(cog.info().band_descriptions)
        >>> [("b1", ""), ("b2", ""), ("b3", "")]

        print(list(cog.statistics()))
        >>> ["b1", "b2", "b3"]

    with STACReader("stac.json") as stac:
        print(stac.tile(701, 102, 8, assets=("green", "red")).band_names)
        >>> ["green_b1", "red_b1"]
    ```

* depreciate `asset_expression` in MultiBaseReader. Use of expression is now possible
* `expression` for MultiBaseReader must be in form of `{asset}_b{index}`

    ```python
    # before
    with STACReader("stac.json") as stac:
        stac.tile(701, 102, 8, expression="green/red")

    # now
    with STACReader("stac.json") as stac:
        stac.tile(701, 102, 8, expression="green_b1/red_b1")
    ```

* `rio_tiler.reader.point()` (and all Reader's point methods) now return a **rio_tiler.models.PointData** object

    ```python
    # before
    with rasterio.open("cog.tif") as src::
        v = rio_tiler.reader.point(10.20, -42.0)
        print(v)
        >>> [0, 0, 0]

    with COGReader("cog.tif") as cog:
        print(cog.point(10.20, -42.0))
        >>> [0, 0, 0]

    # now
    with rasterio.open("cog.tif") as src::
        v = rio_tiler.reader.point(src, (10.20, -42))
        print(v)
        >>> PointData(
            data=array([3744], dtype=uint16),
            mask=array([255], dtype=uint8),
            band_names=['b1'],
            coordinates=(10.20, -42),
            crs=CRS.from_epsg(4326),
            assets=['cog.tif'],
            metadata={}
        )

    with Reader("cog.tif") as cog:
        print(cog.point(10.20, -42.0))
        >>> PointData(
            data=array([3744], dtype=uint16),
            mask=array([255], dtype=uint8),
            band_names=['b1'],
            coordinates=(10.20, -42),
            crs=CRS.from_epsg(4326),
            assets=['cog.tif'],
            metadata={}
        )
    ```

* deleted `rio_tiler.reader.preview` function and updated `rio_tiler.reader.read` to allow width/height/max_size options
* reordered keyword options in all `rio_tiler.reader` function for consistency
* removed `AlphaBandWarning` warning when automatically excluding alpha band from data
* remove `nodata`, `unscale`, `resampling_method`, `vrt_options` and `post_process` options to `Reader` init method and replaced with `options`

    ```python
    # before
    with COGReader("cog.tif", nodata=1, resampling_method="bilinear") as cog:
        data = cog.preview()

    # now
    with Reader(COGEO, options={"nodata": 1, "resampling_method": "bilinear"}) as cog:
        data = cog.preview()
    ```

# 3.1.6 (2022-07-22)

* Hide `NotGeoreferencedWarning` warnings in `utils.render` and `utils.resize_array`
* update `MultiBaseReader` and `MultiBandReader` `points` method to prepare for numpy changes.

# 3.1.5 (2022-07-06)

* Deprecate `rio_tiler.io.GCPCOGReader` and allow GPCS dataset to be opened by `rio_tiler.io.COGReader`

```python
# before
with GCPCOGReader("my.tif") as cog:
    ...

# now, COGReader will find the gcps and create an internal WarpedVRT using the gpcs and crs
with COGReader("my.tif") as cog:
    ...
```

* add `ImageData.rescale` to rescale the array in place
* add `ImageData.apply_color_formula` to apply color formula in place

# 3.1.4 (2022-04-14)

* Fix cutline creation for MultiPolygon (author @Fernigithub, <https://github.com/cogeotiff/rio-tiler/pull/493>)

# 3.1.3 (2022-04-08)

* Switch to `pyproject.toml` and `flit` for packaging (<https://github.com/cogeotiff/rio-tiler/pull/490>)
* Catch discrete colormap with negative values (<https://github.com/cogeotiff/rio-tiler/pull/492>)

# 3.1.2 (2022-03-25)

* avoid calculating statistics for non-finite values (<https://github.com/cogeotiff/rio-tiler/pull/489>)

# 3.1.1 (2022-03-17)

* forward `band names` to ImageData output in `mosaic_reader` (<https://github.com/cogeotiff/rio-tiler/pull/486>)

# 3.1.0 (2022-02-21)

* add support for setting the S3 endpoint url scheme via the `AWS_HTTPS` environment variables in `aws_get_object` function using boto3 (<https://github.com/cogeotiff/rio-tiler/pull/476>)
* Add semicolon `;` support for multi-blocks expression (<https://github.com/cogeotiff/rio-tiler/pull/479>)
* add `rio_tiler.expression.get_expression_blocks` method to split expression (<https://github.com/cogeotiff/rio-tiler/pull/479>)
* add `merged_statistics` method for `MultiBaseReader` to get statistics using between assets expression (<https://github.com/cogeotiff/rio-tiler/pull/478>)

**future deprecation**

* using a comma `,` in an expression to define multiple blocks will be replaced by semicolon `;`

```python
# before
expression = "b1+b2,b2"

# new
expression = "b1+b2;b2"
```

**breaking changes**

* update morecantile requirement to `>=3.1,<4.0`. WebMercatorQuad TMS is now aligned with GDAL and Mercantile TMS definition.

# 3.0.3 (2022-01-18)

* make sure we raise an HTTP exception when using an invalid STAC url (<https://github.com/cogeotiff/rio-tiler/pull/475>)

# 3.0.2 (2022-01-03)

* switch from `functools.lru_cache` to `cachetools.LRUCache` to allow unashable options in `rio_tiler.io.stac.fetch` function (<https://github.com/cogeotiff/rio-tiler/pull/471>)

# 3.0.1 (2021-12-03)

* avoid useless call to `transform_bounds` if input/output CRS are equals (<https://github.com/cogeotiff/rio-tiler/pull/466>)
* make sure `geographic_bounds` don't return inf or nan values (<https://github.com/cogeotiff/rio-tiler/pull/467>)

# 3.0.0 (2021-11-29)

* no change since `3.0.0a6`

# 3.0.0a6 (2021-11-22)

* add `rio_tiler.utils.resize_array` to resize array to a given width/height (<https://github.com/cogeotiff/rio-tiler/pull/463>)
* use `resize_array` in `ImageData.create_from_list` to avoid trying merging array of different sizes (<https://github.com/cogeotiff/rio-tiler/pull/463>)

**breaking changes**

* update `MultiBaseReader` and `MultiBandReader` to be their own abstract classes instead of being subclass of `BaseReader`.
* put `reader` attribute outside of the `__init__` method for `MultiBaseReader` and `MultiBandReader`.

# 3.0.0a5 (2021-11-18)

* allow the definition of `geographic_crs` used in the `geographic_bounds` property (<https://github.com/cogeotiff/rio-tiler/pull/458>)
* use `contextlib.ExitStack` to better manager opening/closing rasterio dataset (<https://github.com/cogeotiff/rio-tiler/pull/459>)
* moves `BBox, ColorTuple, Indexes, NoData, NumType` type definitions in `rio_tiler.types` (<https://github.com/cogeotiff/rio-tiler/pull/460>)
* better types definition for ColorMap objects (<https://github.com/cogeotiff/rio-tiler/pull/460>)
* fix some types issues (<https://github.com/cogeotiff/rio-tiler/pull/460>)

# 3.0.0a4 (2021-11-10)

* refactor `SpatialMixin.tile_exists` to compare the bounds in the dataset's coordinate system to avoid coordinates overflow (a TMS CRS bounds can be smaller than the dataset CRS bounds) (<https://github.com/cogeotiff/rio-tiler/pull/455>)

# 3.0.0a3 (2021-11-03)

* Reader's `info` and `statistics` methods to default to available `bands` or `assets` if not provided (<https://github.com/cogeotiff/rio-tiler/pull/451>)

# 3.0.0a2 (2021-10-21)

* Allow `rio_tiler.utils.get_array_statistics` to return `0` for unfound category, instead of raising an error (<https://github.com/cogeotiff/rio-tiler/pull/443>)

# 3.0.0a1 (2021-10-20)

**breaking changes**

* add `input` in BaseReader class definition to avoid type mismatch (<https://github.com/cogeotiff/rio-tiler/pull/450>)

    Note: `input` replaces `filepath` attribute in STACReader and COGReader.

**removed**

* * `rio_tiler.models.ImageStatistics` model

# 3.0.0a0 (2021-10-19)

* add `crs` property in `rio_tiler.io.base.SpatialMixin` (<https://github.com/cogeotiff/rio-tiler/pull/429>)
* add `geographic_bounds` in `rio_tiler.io.base.SpatialMixin` to return bounds in WGS84 (<https://github.com/cogeotiff/rio-tiler/pull/429>)

```python
from rio_tiler.io import COGReader

with COGReader("https://rio-tiler-dev.s3.amazonaws.com/data/fixtures/cog.tif") as cog:
    print(cog.bounds)
    >> (373185.0, 8019284.949381611, 639014.9492102272, 8286015.0)

    print(cog.crs)
    >> "EPSG:32621"

    print(cog.geographic_bounds)
    >> (-61.28762442711404, 72.22979795551834, -52.301598718454485, 74.66298001264106)
```

* Allow errors to be ignored when trying to find `zooms` for dataset in `rio_tiler.io.COGReader`. If we're not able to find the zooms in selected TMS, COGReader will defaults to the min/max zooms of the TMS (<https://github.com/cogeotiff/rio-tiler/pull/429>)

```python
from pyproj import CRS
from morecantile import TileMatrixSet

from rio_tiler.io import COGReader

# For a non-earth dataset there is no available transformation from its own CRS and the default WebMercator TMS CRS.
with COGReader("https://rio-tiler-dev.s3.amazonaws.com/data/fixtures/cog_nonearth.tif") as cog:
    >> UserWarning: Cannot determine min/max zoom based on dataset information, will default to TMS min/max zoom.

    print(cog.minzoom)
    >> 0

    print(cog.maxzoom)
    >> 24

# if we use a `compatible TMS` then we don't get warnings
europa_crs = CRS.from_authority("ESRI", 104915)
europa_tms = TileMatrixSet.custom(
    crs=europa_crs,
    extent=europa_crs.area_of_use.bounds,
    matrix_scale=[2, 1],
)
with COGReader(
    "https://rio-tiler-dev.s3.amazonaws.com/data/fixtures/cog_nonearth.tif",
    tms=europa_tms,
) as cog:
    print(cog.minzoom)
    >> 4

    print(cog.maxzoom)
    >> 6
```

* compare dataset bounds and tile bounds in TMS crs in `rio_tiler.io.base.SpatialMixin.tile_exists` method to allow dataset and TMS not compatible with WGS84 crs (<https://github.com/cogeotiff/rio-tiler/pull/429>)
* use `httpx` package instead of requests (author @rodrigoalmeida94, <https://github.com/cogeotiff/rio-tiler/pull/431>)
* allow **half pixel** `tile_buffer` around the tile (e.g 0.5 -> 257x257, 1.5 -> 259x259) (author @bstadlbauer, <https://github.com/cogeotiff/rio-tiler/pull/405>)
* add support for **intervals** colormap (<https://github.com/cogeotiff/rio-tiler/pull/439>))

```python
from rio_tiler.colormap import apply_cmap, apply_intervals_cmap

data = numpy.random.randint(0, 255, size=(1, 256, 256))
cmap = [
    # ([min, max], [r, g, b, a])
    ([0, 1], [0, 0, 0, 0]),
    ([1, 10], [255, 255, 255, 255]),
    ([10, 100], [255, 0, 0, 255]),
    ([100, 256], [255, 255, 0, 255]),
]

data, mask = apply_intervals_cmap(data, cmap)
# or
data, mask = apply_cmap(data, cmap)
```

**breaking changes**

* update morecantile requirement to version >=3.0 (<https://github.com/cogeotiff/rio-tiler/pull/418>)
* remove python 3.6 support (<https://github.com/cogeotiff/rio-tiler/pull/418>)
* remove `max_size` defaults for `COGReader.part` and `COGReader.feature`, which will now default to full resolution reading.

```python
# before
with COGReader("my.tif") as cog:
    img = cog.part(*cog.dataset.bounds, dst_crs=cog.dataset.crs, bounds_crs=cog.dataset.crs)
    # by default image should be max 1024x1024
    assert max(img.width, 1024) # by default image should be max 1024x1024
    assert max(img.height, 1024)

# now (there is no more max_size default)
with COGReader("my.tif") as cog:
    img = cog.part(*cog.dataset.bounds, dst_crs=cog.dataset.crs, bounds_crs=cog.dataset.crs)
    assert img.width == cog.dataset.width
    assert img.height == cog.dataset.height
```

* add `.statistics` method in base classes (<https://github.com/cogeotiff/rio-tiler/pull/427>)

* remove `rio_tiler.io.base.SpatialMixin.spatial_info` and `rio_tiler.io.base.SpatialMixin.center` properties (<https://github.com/cogeotiff/rio-tiler/pull/429>)

* Reader's `.bounds` property should now be in dataset's CRS, not in `WGS84` (<https://github.com/cogeotiff/rio-tiler/pull/429>)

```python
# before
with COGReader("my.tif") as cog:
    print(cog.bounds)
    >>> (-61.287001876638215, 15.537756794450583, -61.27877967704677, 15.542486503997608)

# now
with COGReader("my.tif") as cog:
    print(cog.bounds)
    >>> (683715.3266400001, 1718548.5702, 684593.2680000002, 1719064.90736)

    print(cog.crs)
    >>> EPSG:32620

    print(cog.geographic_bounds)
    >>> (-61.287001876638215, 15.537756794450583, -61.27877967704677, 15.542486503997608)
```

* Use `RIO_TILER_MAX_THREADS` environment variable instead of `MAX_THREADS` (author @rodrigoalmeida94, <https://github.com/cogeotiff/rio-tiler/pull/432>)
* remove `band_expression` in `rio_tiler.io.base.MultiBandReader` (<https://github.com/cogeotiff/rio-tiler/pull/433>)
* change `asset_expression` input type from `str` to `Dict[str, str]` in `rio_tiler.io.base.MultiBaseReader` (<https://github.com/cogeotiff/rio-tiler/pull/434>)

```python
# before
with STACReader("mystac.json") as stac:
    img = stac.preview(
        assets=("data1", "data2"),
        asset_expression="b1*2",  # expression was applied to each asset
    )

# now
with STACReader("mystac.json") as stac:
    img = stac.preview(
        assets=("data1", "data2"),
        asset_expression={"data1": "b1*2", "data2": "b2*100"},  # we can now pass per asset expression
    )
```

* add `asset_indexes` in `rio_tiler.io.base.MultiBaseReader`, which replaces `indexes`. (<https://github.com/cogeotiff/rio-tiler/pull/434>)

```python
# before
with STACReader("mystac.json") as stac:
    img = stac.preview(
        assets=("data1", "data2"),
        indexes=(1,),  # indexes was applied to each asset
    )

# now
with STACReader("mystac.json") as stac:
    img = stac.preview(
        assets=("data1", "data2"),
        asset_indexes={"data1": 1, "data2": 2},  # we can now pass per asset indexes
    )
```

**removed**

* `rio_tiler.io.BaseReader.metadata` and `rio_tiler.io.BaseReader.stats` base class methods (<https://github.com/cogeotiff/rio-tiler/pull/425>)
* `rio_tiler.reader.stats` function (<https://github.com/cogeotiff/rio-tiler/pull/440>)
* `rio_tiler.reader.metadata` function (<https://github.com/cogeotiff/rio-tiler/pull/440>)
* `rio_tiler.utils._stats` function (<https://github.com/cogeotiff/rio-tiler/pull/440>)

# 2.1.3 (2021-09-14)

* Make sure output data is of type `Uint8` when applying a colormap (<https://github.com/cogeotiff/rio-tiler/pull/423>)
* Do not auto-rescale data if there is a colormap (<https://github.com/cogeotiff/rio-tiler/pull/423>)

# 2.1.2 (2021-08-10)

* update type information for mosaics functions (<https://github.com/cogeotiff/rio-tiler/pull/409>)

## 2.1.1 (2021-07-29)

* add support for setting the S3 endpoint url via the `AWS_S3_ENDPOINT` environment variables in `aws_get_object` function using boto3 (<https://github.com/cogeotiff/rio-tiler/pull/394>)
* make `ImageStatistics.valid_percent` a value between 0 and 100 (instead of 0 and 1) (author @param-thakker, <https://github.com/cogeotiff/rio-tiler/pull/400>)
* add `fetch_options` to `STACReader` to allow custom configuration to the fetch client (<https://github.com/cogeotiff/rio-tiler/pull/404>)

    ```python
    with STACReader("s3://...", fetch_options={"request_pays": True}):
        pass
    ```

* Fix alpha band values when storing `Uint16` data in **PNG**. (<https://github.com/cogeotiff/rio-tiler/pull/407>)

## 2.1.0 (2021-05-17)

* add auto-rescaling in `ImageData.render` method to avoid error when datatype is not supported by the output driver (<https://github.com/cogeotiff/rio-tiler/pull/391>)

```python
# before - exit with error
with open("img.png", "wb") as f:
    f.write(ImageData(numpy.zeros((3, 256, 256), dtype="float32")).render())
>>> (ERROR) CPLE_NotSupportedError: "PNG driver doesn't support data type Float32. Only eight bit (Byte) and sixteen bit (UInt16) bands supported".

# now - print a warning
with open("img.png", "wb") as f:
    f.write(ImageData(numpy.zeros((3, 256, 256), dtype="float32")).render())
>>> (WARNING) InvalidDatatypeWarning: "Invalid type: `float32` for the `PNG` driver. Data will be rescaled using min/max type bounds".
```

**breaking changes**

* change type of `in_range` option in `ImageData.render` to `Sequence[Tuple[NumType, NumType]]` (<https://github.com/cogeotiff/rio-tiler/pull/391>)

```python
img = ImageData(numpy.zeros((3, 256, 256), dtype="uint16"))

# before - Tuple[NumType, NumType]
buff = img.render(in_range=(0, 1000, 0, 1000, 0, 1000))

# now - Sequence[Tuple[NumType, NumType]]
buff = img.render(in_range=((0, 1000), (0, 1000), (0, 1000)))
```

## 2.0.8 (2021-04-26)

* add warning when dataset doesn't have overviews (<https://github.com/cogeotiff/rio-tiler/pull/386>)
* add `width`, `height`, `count` and `overviews` infos in `COGReader.info()` (<https://github.com/cogeotiff/rio-tiler/pull/387>)
* add `driver` in `COGReader.info()` output (<https://github.com/cogeotiff/rio-tiler/pull/388>)
* add `valid_percent` in `stats` output (<https://github.com/cogeotiff/rio-tiler/pull/389>)

## 2.0.7 (2021-04-01)

* use importlib.resources `.files` method to resolve the package directory (<https://github.com/cogeotiff/rio-tiler/pull/379>)

## 2.0.6 (2021-03-25)

* add `read()` method in COGReader (<https://github.com/cogeotiff/rio-tiler/pull/366>)
* add `tile_buffer` option to `COGReader.tile()` method to add pixels around a tile request (<https://github.com/cogeotiff/rio-tiler/issues/365>)
* use `importlib.resources.path` to find rio-tiler `cmap_data` directory (<https://github.com/cogeotiff/rio-tiler/pull/370>)
* re-use type definitions (<https://github.com/cogeotiff/rio-tiler/issues/337>)

## 2.0.5 (2021-03-17)

* make sure `py.typed` is included in the package (<https://github.com/cogeotiff/rio-tiler/pull/363>)
* add `jpg` alias in `img_profiles` (<https://github.com/cogeotiff/rio-tiler/pull/364>)

```python
from rio_tiler.profiles import img_profiles

jpeg = img_profiles.get("jpeg")
jpg = img_profiles.get("jpg")
assert jpeg == jpg
```

## 2.0.4 (2021-03-09)

* Added [pystac.MediaType.COG](https://github.com/stac-utils/pystac/blob/master/pystac/media_type.py#L4) in supported types by STAC reader
* fix bad type definition in `rio_tiler.colormap.ColorMaps` data (<https://github.com/cogeotiff/rio-tiler/issues/359>)
* add `rio_tiler.colormap.parse_color` function to parse HEX color (<https://github.com/cogeotiff/rio-tiler/issues/361>)

## 2.0.3 (2021-02-19)

* Reduce the number of `.read()` calls for dataset without nodata value (<https://github.com/cogeotiff/rio-tiler/pull/355>)
* replace deprecated `numpy.float` by `numpy.float64`

## 2.0.2 (2021-02-17)

* fix bad mask datatype returned by mosaic methods (<https://github.com/cogeotiff/rio-tiler/pull/353>)
* align WarpedVRT with internal blocks when needed. This is to reduce the number of GET requests need for VSI files (<https://github.com/cogeotiff/rio-tiler/pull/345>)

## 2.0.1 (2021-02-04)

* fix arguments names conflicts between mosaic_reader/tasks and STACReader options (<https://github.com/cogeotiff/rio-tiler/pull/343>)
* update rio-tiler pypi description.

## 2.0.0 (2021-01-27)

* add MultiPolygon support in `rio_tiler.utils.create_cutline` (<https://github.com/cogeotiff/rio-tiler/issues/323>)
* support discrete colormap by default in `apply_cmap` (<https://github.com/cogeotiff/rio-tiler/issues/321>)
* delete deprecated `rio_tiler.mercator` submodule
* added default factory in `rio_tiler.colormap.ColorMaps`.
* fix missing `metadata` forwarding in `ImageData.post_process` method.
* refactor `rio_tiler.io.GCPCOGReader` for better inheritance from COGReader.

**breaking change**

* renamed input parameter `tile` to `data` in `rio_tiler.utils.render`.
* renamed input parameter `arr` to `data` in `rio_tiler.utils.mapzen_elevation_rgb`
* made `rio_tiler.io.stac.to_pystac_item` private (renamed to `_to_pystac_item`)
* renamed `rio_tiler.colormap.DEFAULTS_CMAPS` to `rio_tiler.colormap.DEFAULT_CMAPS_FILES`
* made `rio_tiler.reader._read` public (renamed to rio_tiler.reader.read) (ref: <https://github.com/cogeotiff/rio-tiler/issues/332>)

## 2.0.0rc4 (2020-12-18)

* add `NPZ` output format (<https://github.com/cogeotiff/rio-tiler/issues/308>)
* add [pystac](https://pystac.readthedocs.io/en/latest/) for STAC item reader (author @emmanuelmathot, <https://github.com/cogeotiff/rio-tiler/issues/212>)
* delete deprecated function: `rio_tiler.reader.tile`, `rio_tiler.utils.tile_exits` and `rio_tiler.utils.geotiff_options`
* deprecated `rio_tiler.mercator` submodule (<https://github.com/cogeotiff/rio-tiler/issues/315>)
* update morecantile version to 2.1, which has better `tms.zoom_for_res` definition.

## 2.0.0rc3 (2020-11-24)

* add `feature` method to reader classes (<https://github.com/cogeotiff/rio-tiler/issues/306>)

## 2.0.0rc2 (2020-11-17)

* add `data` validation in `rio_tiler.models.ImageData` model. Data MUST be a 3 dimensions array in form of (count, height, width).
* `mask` is now optional for `rio_tiler.models.ImageData` model, but will be initialized to a default full valid (`255`) array.

```python
import numpy
from rio_tiler.models import ImageData

data = numpy.random.rand(3, 10, 10)

img = ImageData(data)
assert img.mask.all()
```

* add `metadata` property to `rio_tiler.models.ImageData` model

```python
img.metadata
>>> {}
```

**breaking change**

* `rio_tiler.mosaic.reader.mosaic_reader` now raises `EmptyMosaicError` instead of returning an empty `ImageData`

## 2.0.0rc1.post1 (2020-11-12)

* Remove `Uint8` data casting before applying `color_formula` in ImageData.render (<https://github.com/cogeotiff/rio-tiler/issues/302>)

## 2.0.0rc1 (2020-11-09)

* added `ImageData` output class for all `rio_tiler.io` classes returning numpy array-like types (`tile, mask = method()`)

```python
from rio_tiler.io import COGReader
from rio_tiler.models import ImageData

with COGReader("/Users/vincentsarago/S-2_20200422_COG.tif") as cog:
    r = cog.preview()
    assert isinstance(r, ImageData)

    data, mask = r
    assert data.shape == (3, 892, 1024)
```

**Note**: the class keeps the compatibility with previous notation: `tile, mask = ImageData`

* add pydantic models for IO outputs (Metadata, Info, ...)

* change output form for `band_metadata`, `band_descriptions` and do not add band description when not found.

```python
# Before
with COGReader("/Users/vincentsarago/S-2_20200422_COG.tif") as cog:
    i = cog.info()
    print(i["band_metadata"])
    print(i["band_descriptions"])

[(1, {}), (2, {}), (2, {})]
[(1, 'band1'), (2, 'band2'), (2, 'band3')]

# Now
with COGReader("/Users/vincentsarago/S-2_20200422_COG.tif") as cog:
    i = cog.info()
    print(i.band_metadata)
    print(i.band_descriptions)

[('1', {}), ('2', {}), ('3', {})]
[('1', ''), ('2', ''), ('3', '')]
```

* change output form for `stats`

```python
# Before
with COGReader("/Users/vincentsarago/S-2_20200422_COG.tif") as cog:
    print(cog.stats())
{
    1: {...},
    2: {...},
    3: {...}
}

# Now
with COGReader("/Users/vincentsarago/S-2_20200422_COG.tif") as cog:
    print(cog.stats())
{
    "1": {...},
    "2": {...},
    "3": {...}
}
```

* updated `rio_tiler.utils._stats` function to replace `pc` by `percentiles`

```python
with COGReader("/Users/vincentsarago/S-2_20200422_COG.tif") as cog:
    print(cog.stats()["1"].json())
{"percentiles": [19.0, 168.0], "min": 0.0, "max": 255.0, ...}
```

* make `rio_tiler.colormap.ColorMap` object immutable. Registering a new colormap will new returns a now instance of ColorMap(<https://github.com/cogeotiff/rio-tiler/issues/289>).
* changed the `rio_tiler.colormap.ColorMap.register()` method to take a dictionary as input (instead of name + dict).

```python
from rio_tiler.colormap import cmap # default cmap

# previous
cmap.register("acmap", {0: [0, 0, 0, 0], ...})

# Now
cmap = cmap.register({"acmap": {0: [0, 0, 0, 0], ...}})
```

* added the possibility to automatically register colormaps stored as `.npy` file in a directory, if `COLORMAP_DIRECTORY` environment variable is set with the name of the directory.

* Update to morecantile 2.0.0

## 2.0.0b19 (2020-10-26)

* surface `allowed_exceptions` options in `rio_tiler.mosaic.reader.mosaic_reader` (<https://github.com/cogeotiff/rio-tiler/issues/293>)
* add SpatialInfoMixin base class to reduce code duplication (co-author with @geospatial-jeff, <https://github.com/cogeotiff/rio-tiler/pull/295>)
* add `AsyncBaseReader` to support async readers (author @geospatial-jeff, <https://github.com/cogeotiff/rio-tiler/pull/265>)

## 2.0.0b18 (2020-10-22)

* surface dataset.nodata in COGReader.nodata property (<https://github.com/cogeotiff/rio-tiler/pull/292>)
* fix non-threaded tasks scheduler/filter (<https://github.com/cogeotiff/rio-tiler/pull/291>)

## 2.0.0b17 (2020-10-13)

* switch to morecantile for TMS definition (ref: <https://github.com/cogeotiff/rio-tiler/issues/283>)
* add tms options in Readers (breaking change if you create custom Reader from BaseReader)
* add tile_bounds vs bounds check in tile methods for MultiBands and MultiBase classes
* add tile_exists method in BaseReader (take tms in account)
* adapt zooms calculation in COGReader
* add `LastBandHigh` and `LastBandLow` pixel selection (ref: <https://github.com/cogeotiff/rio-tiler/pull/270>)

Deprecated function

* rio_tiler.reader.tile
* rio_tiler.utils.geotiff_options
* rio_tiler.utils.tile_exists
* rio_tiler.io.multi_*

## 2.0.0b16 (2020-10-07)

* remove `pkg_resources` (<https://github.com/pypa/setuptools/issues/510>)
* refactor default colormap lookup to use pathlib instead of pkg_resources.

Note: We changed the versioning scheme to `{major}.{minor}.{path}{pre}{prenum}`

## 2.0b15 (2020-10-05)

* Fix missing Exception catching when running task outside threads (ref: <https://github.com/developmentseed/titiler/issues/130>).
* add rio-tiler logger (<https://github.com/cogeotiff/rio-tiler/issues/277>).

## 2.0b14.post2 (2020-10-02)

* Fix bug in `MultiBandReader` (ref: <https://github.com/cogeotiff/rio-tiler/issues/275>) and add tests.

## 2.0b14.post1 (2020-10-02)

* add `MultiBandReader` and `GCPCOGReader` in `rio_tiler.io` init.

## 2.0b14 (2020-10-02)

* Added back the Conctext Manager methods in `rio_tiler.io.base.BaseReader` but not as `@abc.abstractmethod` (ref: <https://github.com/cogeotiff/rio-tiler/pull/273#discussion_r498937943>)
* Move `rio_tiler_pds.reader.MultiBandReader` and `rio_tiler_pds.reader.GCPCOGReader` to rio-tiler (<https://github.com/cogeotiff/rio-tiler/pull/273>)

## 2.0b13 (2020-10-01)

* remove ContextManager requirement for `rio_tiler.io.base.BaseReader` and `rio_tiler.io.base.MultiBaseReader` base classes.
* move ContextManager properties definition to `__attrs_post_init__` method in `rio_tiler.io.STACReader` and `rio_tiler.io.COGReader` (ref: <https://github.com/cogeotiff/rio-tiler-pds/issues/21>)

## 2.0b12 (2020-09-28)

* Make sure Alpha band isn't considered as an internal mask by `utils.has_mask_band`

## 2.0b11 (2020-09-24)

* reduce verbosity in `rio_tiler.tasks.filter_tasks` exception logging (#266).

2.0b10 (2020-09-15)
------------------

- add `post_process` callback to `rio_tiler.render._read` and `rio_tiler.render.point` to apply
specific operation ouput arrays.

2.0b9 (2020-09-09)
------------------

- restore Mkdocs search bar (#255)
* Allow class (not just instance) to be passed to pixel_selection (#250)
* Add Binder link/badge to README (#254)
* Add mkdocs-jupyter to show notebooks in website (#253)
* Remove deprecated functions (#247)
* Export modules from top-level package (#246)
* Allow overwriting colormap with force=True (#249)
* Pin black version (#251)
* Add contributing.md (#242)
* Add mkdocs config (#240)
* Add `NPY` support in `rio_tiler.utils.render` to save tile in numpy binary format (#256)
* Remove bare `Exception` and add more detailed errors (#248)

2.0b8 (2020-08-24)
------------------

- raise specific `PointOutsideBounds` in rio_tiler.reader.point (#236)

2.0b7 (2020-08-21)
------------------

- allow setting default kwargs in COGReader **init** (#227)
* allow `vrt_options` in COGReader.point
* add `rio_tiler.io.base.MultiBaseReader` class (#225)
* refactor `rio_tiler.io.stac.STACReader` to use MultiBaseReader (#225)
* add `rio_tiler.task` submodule to share tools for handling rio-tiler's future tasks.
* fix regex parsing for rio-tiler expression
* add warnings when assets/indexes is passed with expression option (#233)

Breaking Changes:
* replace dataclass wiht attr to support more flexible class definition (see #225)

2.0b6 (2020-08-04)
------------------

- add `utils.create_cutline` helper (#218)
* remove any mutable default argument

**depreciation**
* `warp_vrt_option` is replaced by `vrt_options` in rio_tiler.reader.part (#221)

2.0b5 (2020-07-31)
------------------

- add more verbosity to mosaic error (#214)

Breaking Changes:
* `rio_tiler.mosaic.reader.mosaic_reader` return `((tile, mask), assets_used)`
* `COGReader.info` is now a method instead of a property to align with other reader (#211)

2.0b4 (2020-07-30)
------------------

- add rio_tiler.io.base.BaseReader abstract class for COGReader and STACReader to inherit from
* STACReader raises `InvalidAssetName` for invalid asset name or `MissingAssets` when no assets is passed (#208)
* update rio_tiler.mosaic.reader.mosaic_reader to not use threadPool if threads <= 1 (#207)

Breaking Changes:
* Reader.spatial_info is a property (#203)
* assets is a keyword argument in STACReader stats/info/metadata

2.0b3 (2020-07-27)
------------------

- add `rio_tiler.mosaic` submodule (ref: <https://github.com/cogeotiff/rio-tiler-mosaic/issues/16>)

2.0b2 (2020-07-23)
------------------

- add boto3 in the dependency (#201)

2.0b1 (2020-07-22)
------------------

- switch to ContextManager for COG and STAC (rio_cogeo.io.COGReader, rio_cogeo.io.STACReader).
* COGReader.part and STACReader.part return data in BBOX CRS by default.
* STACReader now accept URL (https, s3).
* add more method for STAC (prewiew/point/part/info/stats).
* add expression for COG/STAC preview/point/part.
* add `masked` option in `rio_tiler.reader.point` to control weither or not it should return None or a value.
* remove mission specific tilers (#195).
* remove `rio_tiler.reader.multi_*` functions (replaced by rio_tiler.io.cogeo.multi_*).
* remove `rio_tiler.utils.expression` (replaced by expression options in tilers).

2.0a11 (2020-05-29)
------------------

- refactor `rio_tiler.utils.tile_exists` to allow raster bounds latitude == -90,90

2.0a10 (2020-05-29)
------------------

- Change default resampling to nearest for `_read` (#187)
* add `rio_tiler.reader.stats` (return only array statistics)
* remove default `dst_crs` in `rio_tiler.reader.part` to to fallback to dataset CRS.

2.0a9 (2020-05-27)
------------------

- Refactor colormap and add method to register custom colormap

2.0a8 (2020-05-25)
------------------

- add `preview` method to `rio_tiler.io.cogeo`

2.0a7 (2020-05-17)
------------------

- allow reading high resolution part of a raster (by making height, width args optional)
* add `max_size` option in `rio_tiler.reader.part` to set a maximum output size when height and width are not set
* add point and area function in rio_tiler.io.cogeo
* fix width-height height-widht bug in `rio_tiler.reader.part`

**depreciation**
* deprecated `out_window` option in favor of `window` in rio_tiler.reader._read

2.0a6 (2020-05-06)
------------------

- fix unwanted breacking change with `img_profiles.get` not allowing default values

2.0a5 (2020-05-06)
------------------

- make `rio_tiler.io.landsat8.tile` return Uint16 data and not float32 (#173)
* `rio_tiler.profiles.img_profiles` item access return `copy` of the items (#177)
* better colormap docs (#176, author @kylebarron)

2.0a4 (2020-04-08)
------------------

- add `rio_tiler.io.cogeo.info` to retrieve simple file metadata (no image statistics)
* add band metadata tag info in `rio_tiler.render.metadata` output
* add `rio_tiler.io.stac` STAC compliant rio_tiler.colormap.apply_discrete_cmap

2.0a3 (2020-03-25)
------------------

- only use `transform_bounds` when needed in rio_tiler.reader.part

Breaking Changes:
* switch back to gdal/rasterio calculate_default_transform (#164). Thanks to Terracotta core developper @dionhaefner.
* refactor `rio_tiler.utils.get_vrt_transform` to get width and height input.

2.0a2 (2020-03-20)
------------------

- Fall back to gdal/rasterio calculate_default_transform for dateline separation crossing dataset (ref #164)

2.0a1 (2020-03-19)
------------------

- added `reader.preview`, `reader.point` methods
* added multi_* functions to rio_tiler.reader to support multiple assets addresses
* added `rio_tiler.utils.has_mask_band` function
* added `rio_tiler.utils.get_overview_level` to calculate the overview level needed for partial reading.
* added type hints
* added scale, offsets, colormap, datatype and colorinterp in reader.metadata output (#158)
* new `rio_tiler.colormap` submodule
* added `unscale` options to rio_tiler.reader._read function apply internal scale/offset (#157)

Breaking Changes:
* removed python 2 support
* new package architecture (.io submodule)
* introduced new rio_tiler.reader functions (part, preview, metadata...)
* renamed rio_tiler.main to rio_tiler.io.cogeo
* bucket and prefixes are defined in rio_tiler.io.dataset.`{dataset}_parse` function from
  AWS supported Public Dataset
* renamed `minimum_tile_cover` to `minimum_overlap`
* renamed `tile_edge_padding` to `padding`
* padding is set to 0 by default.
* use terracotta calculate_default_transform (see <https://github.com/cogeotiff/rio-tiler/issues/56#issuecomment-442484999>)
* colormaps are now have an alpha value
* `rio_tiler.utils.get_colormap` replaced by `rio_tiler.colormap.get_colormap`
* new `rio_tiler.colormap.get_colormap` supports only GDAL like colormap
* replaced `rio_tiler.utils.array_to_image` by `rio_tiler.utils.render`
* replaced `rio_tiler.utils.apply_cmap` by `rio_tiler.colormap.apply_cmap`
* replaced `rio_tiler.utils._apply_discrete_colormap` by `rio_tiler.colormap.apply_discrete_cmap`
* removed `histogram_bins` and `histogram_range` in options in metadata reader.
  Should now be passed in `hist_options` (e.g: hist_options={bins=10, range=(0, 10)})
* remove alpha band value from output data array in tile/preview/metadata #127

1.4.0 (2020-02-19)
------------------

- Add Sentinel2-L2A support (#137)
* Update Sentinel-2 sceneid schema (S2A_tile_20170323_07SNC_0 -> S2A_L1C_20170323_07SNC_0)

1.3.1 (2019-11-06)
------------------

- Add `warp_vrt_option` option for `utils.raster_get_stats` and `utils.tile_read` to
allow more custom VRT Warping. (ref: <https://github.com/OSGeo/gdal/issues/1989#issue-518526399>)
* Add `rio_tiler.utils.non_alpha_indexes` to find non-alpha band indexes (ref #127)

1.3.0 (2019-10-07)
------------------

- Allow `DatasetReader`, `DatasetWriter`, `WarpedVRT` input for `utils.raster_get_stats` and `utils.tile_read`
* add `minimum_tile_cover` option to filter dataset not covering a certain amount of the tile.
* add Sentinel-1 submodule

Breaking Changes:
* need rasterio>=1.1

1.2.11 (2019-09-18)
-------------------

- reduce memory footprint of expression tiler
* fix wrong calculation for overview size in `raster_get_stats` (#116)
* Add Landsat 8 QA Band (#117).

1.2.10 (2019-07-18)
-------------------

- add more colormap options (from matplotlib) and switch from txt files to numpy binaries (#115)

1.2.9 (2019-07-11)
------------------

- fix issue #113, adds depreciation warning for `bounds_crs` in favor of `dst_crs`
in `rio_tiler.utils.get_vrt_transform`

1.2.8 (2019-07-08)
------------------

- Add kwargs options in landsat8.tile, sentinel2.tile and cbers.tile functions to
allow `resampling_method` and `tile_edge_padding` options forwarding to utils._tile_read.
* Add Input (bounds_crs) and Output (dst_crs) option to `utils._tile_read` function (#108)

1.2.7 (2019-05-14)
------------------

- Revert changes introduced in #106 (see #105)
* Refactor tests

1.2.6 (2019-05-10) - DELETED
------------------

- Use same resampling method for mask and for data (#105)

1.2.5 (2019-05-08)
------------------

- add tile_edge_padding option to be passed to rio_tiler.utils._tile_read to reduce sharp edges that occur due to resampling (#104)

1.2.4 (2019-04-16)
------------------

- add histogram_range options to be passed to rio_tiler.{module}.metadata function (#102)

1.2.3 (2019-04-04)
------------------

- add histogram_bins options to be passed to rio_tiler.{module}.metadata function (#98)

Bug fixes:
* return index number with band descriptions (#99)

1.2.2 (2019-04-03)
------------------

- add mercator min/max zoom info in metadata output from rio_tiler.utils.raster_get_stats (#96)
* add band description (band name) in metadata output from rio_tiler.utils.raster_get_stats (#96)

1.2.1 (2019-03-26)
------------------

- Replace rio-pansharpen dependency with a fork of the brovey function directly
into `rio_tiler.utils` (rio-pansharpen is unmaintened and not compatible with
rasterio>=1) (#94).

1.2.0 (2019-03-26)
------------------

- `rio_tiler.utils.array_to_image`'s color_map arg can be a dictionary of discrete values (#91)

Breaking Changes:
* `expr` argument is now a required option in `rio_tiler.utils.expression`. (#88)

1.1.4 (2019-03-11)
------------------

- Add 'rplumbo' colormap (#90 by @DanSchoppe)

1.1.3 (2019-03-06)
------------------

Bug fixes:
* Fix casting to integer for MAX_THREADS environment variable.

1.1.1 (2019-02-21)
------------------

- Minor typo correction and harmonization of the use of src/src_dst/src_path in `rio_tiler.utils`

Bug fixes:
* Fix nodata handling in `utils.raster_get_stats`

1.1.0 (2019-02-15)
------------------

- Allow options forwarding to `tile_read` from `main.tile` function (#86)
* Add `resampling_method` options in `rio_tiler.utils.tile_read` to allow user set
resampling. Default is now bilinear (#85)

Bug fixes:
* Fix nodata option forwarding to tile_read when source is a path (#83)

Refactoring:
* Refactor `rio_tiler.utils.tile_read` to reduce code complexity (#84)

Breaking Changes:
* `indexes` options is now set to **None** in `rio_tiler.utils.tile_read`.
Default will now be the dataset indexes.

1.0.1 (2019-02-14)
------------------

- Fix mask datatype bug in `rio_tiler.utils.array_to_image`(#79)
* Fix nodata handling and better test for the nodata/mask main module (#81)

1.0.0 (2019-02-11)
------------------

- add missing Landsat panchromatic band (08) min/max fetch in `rio_tiler.landsat8.metadata` (#58)
* add pre-commit for commit validation (#64)
* code formatting using Black (the uncompromising Python code formatter) (#64)
* update documentation (Sentinel-2 cost) (#68)
* add `utils.raster_get_stats` and `utils._get_stats` to replace `min_max*` function
and to return more statistics (#66)
* add overview level selection to statistical functions to reduce the data download (#59)
* add pure GDAL `array_to_image` function to replace PIL tools (#29)
* add GDAL format output from `utils.get_colormap` to be used in `array_to_image` (#29)
* add GDAL compatible Image creation profile (#29)
* add max threads number settings via "MAX_THREADS" environment variable (#71)

Breaking Changes:
* update `metadata` structure returned by `landsat8.metadata`, `sentinel2.metadata`, `cbers.metadata`
* force sentinel, landsat and cbers band names to be string and add validation (#65)
* moved landsat utility functions from `rio_tiler.utils` to `rio_tiler.landsat8`
  * rio_tiler.utils.landsat_get_mtl -> rio_tiler.landsat8._landsat_get_mtl
  * rio_tiler.utils.landsat_parse_scene_id -> rio_tiler.landsat8._landsat_parse_scene_id
  * rio_tiler.utils.landsat_get_stats -> rio_tiler.landsat8._landsat_stats
* moved cbers utility functions from `rio_tiler.utils` to `rio_tiler.cbers`
  * rio_tiler.utils.cbers_parse_scene_id -> rio_tiler.cbers._cbers_parse_scene_id
* moved sentinel-2 utility functions from `rio_tiler.utils` to `rio_tiler.sentinel2`
  * rio_tiler.utils.sentinel_parse_scene_id -> rio_tiler.sentinel2._sentinel_parse_scene_id
* removed deprecated PIL support as well as base64 encoding function in rio_tiler.utils
  * rio_tiler.utils.img_to_buffer
  * rio_tiler.utils.array_to_img
  * rio_tiler.utils.b64_encode_img
* removed deprecated min_max* functions (landsat_min_max_worker and band_min_max_worker)

1.0rc2 (2018-08-22)
-------------------

- add test case for pix4d nodata+alpha band data

1.0rc1 (2018-07-16)
-------------------

- rasterio 1.0.0

1.0b3 (2018-07-02)
------------------

- add schwarzwald color palette

1.0b2 (2018-06-26)
------------------

- fix nodata (#48)

1.0b1 (2018-06-23)
------------------

- adapt to rasterio 1.0b4
* fix mask (internal/external) fetching 🙏
* fix boundless read with new rasterio 1.0b2
* fix custom nodata handling
* fix performances issue

Breaking Changes:
* removed alpha band options to select a custom alpha band number

1.0a8 (2018-06-20)
------------------

- Fix rasterio version to 1.0b1 (#46 and #44)

1.0a7 (2018-05-14)
------------------

- Support for additional CBERS instruments (fredliporace)

1.0a6 (2018-03-29)
------------------

- Fixes sentinel-2 band 8A regex bug in `rio_tiler.utils.expression`

1.0a5 (2018-03-26)
------------------

- adds DatasetReader input option for utils.tile_read (do not close the dataset on each read)

Breaking Changes:
* `utils.tile_band_worker` renamed to `utils.tile_read`
* `main.tile` **rgb** option renamed **indexes**
* `sentinel2.tile`, `landsat8.tile`,  `cbers.tile` **rgb** option renamed **bands**
* `main.tile` default nodata mask is handled by rasterio

1.0a4 (2018-03-07)
------------------

- adds utils.b64_encode_img function to encode an image object into a base64 string
* add tiles profiles (jpeg, png, webp) based on <https://github.com/mapnik/mapnik/wiki/Image-IO#default-output-details>

Breaking Changes:
* Refactor `rio_tiler.utils.array_to_img` to return PIL image object

1.0a3 (2018-02-05)
------------------

- only using `read_masks` for mask creation when it's needed.

1.0a2 (2018-02-05)
------------------

- add "expression" utility function
* better nodata/mask/alpha band definition and support

Breaking Changes:
* tile functions now return an associated mask (Landsat, Sentinel, CBERS, main)
* remove nodata support in utils.image_to_array function
* add mask support in utils.image_to_array function
* utils.tile_band_worker will always return a (Band, Width, Height) array (e.g 1x256x256 or 3x256x256)

1.0a1 (2018-01-04)
------------------

- remove aws.py sub-module (replaced by main.py)
* no default bands value for main.py tiles.

1.0a.0 (2018-01-03)
------------------

- add colormap option in `utils.array_to_img`
* add TIR (brightness temps) support
* add CBERS support
* add global file support
* add elevation encoding for mapzen
* removing internal caching
* update to rasterio 1.0a12

Breaking Changes:
* remove data value rescaling in `landsat8.tile` and `sentinel2.tile`
* fix wrong lat/grid_square value in `utils.sentinel_parse_scene_id`
* rename `utils.sentinel_min_max_worker` to `utils.band_min_max_worker`

0.0.3 (2017-11-14)
------------------

- Fix Sentinel-2 bad AWS url

0.0.2 (2017-10-17)
------------------

- Fix python 2/3 compatibilities in rio_tiler.utils.landsat_get_mtl

0.0.1 (2017-10-05)
------------------

- Initial release. Requires Rasterio >= 1.0a10.
