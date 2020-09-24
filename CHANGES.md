## 2.0b11 (2020-09-24)

* reduce verbosity in `rio_tiler.tasks.filter_tasks` exception logging (#266).

2.0b10 (2020-09-15)
------------------
- add `post_process` callback to `rio_tiler.render._read` and `rio_tiler.render.point` to apply
specific operation ouput arrays.

2.0b9 (2020-09-09)
------------------
- restore Mkdocs search bar (#255)
- Allow class (not just instance) to be passed to pixel_selection (#250)
- Add Binder link/badge to README (#254)
- Add mkdocs-jupyter to show notebooks in website (#253)
- Remove deprecated functions (#247)
- Export modules from top-level package (#246)
- Allow overwriting colormap with force=True (#249)
- Pin black version (#251)
- Add contributing.md (#242)
- Add mkdocs config (#240)
- Add `NPY` support in `rio_tiler.utils.render` to save tile in numpy binary format (#256)
- Remove bare `Exception` and add more detailed errors (#248)

2.0b8 (2020-08-24)
------------------
- raise specific `PointOutsideBounds` in rio_tiler.reader.point (#236)

2.0b7 (2020-08-21)
------------------
- allow setting default kwargs in COGReader __init__ (#227)
- allow `vrt_options` in COGReader.point
- add `rio_tiler.io.base.MultiBaseReader` class (#225)
- refactor `rio_tiler.io.stac.STACReader` to use MultiBaseReader (#225)
- add `rio_tiler.task` submodule to share tools for handling rio-tiler's future tasks.
- fix regex parsing for rio-tiler expression
- add warnings when assets/indexes is passed with expression option (#233)

Breaking Changes:
- replace dataclass wiht attr to support more flexible class definition (see #225)

2.0b6 (2020-08-04)
------------------
- add `utils.create_cutline` helper (#218)
- remove any mutable default argument

**depreciation**
- `warp_vrt_option` is replaced by `vrt_options` in rio_tiler.reader.part (#221)

2.0b5 (2020-07-31)
------------------
- add more verbosity to mosaic error (#214)

Breaking Changes:
- `rio_tiler.mosaic.reader.mosaic_reader` return `((tile, mask), assets_used)`
- `COGReader.info` is now a method instead of a property to align with other reader (#211)

2.0b4 (2020-07-30)
------------------
- add rio_tiler.io.base.BaseReader abstract class for COGReader and STACReader to inherit from
- STACReader raises `InvalidAssetName` for invalid asset name or `MissingAssets` when no assets is passed (#208)
- update rio_tiler.mosaic.reader.mosaic_reader to not use threadPool if threads <= 1 (#207)

Breaking Changes:
- Reader.spatial_info is a property (#203)
- assets is a keyword argument in STACReader stats/info/metadata

2.0b3 (2020-07-27)
------------------
- add `rio_tiler.mosaic` submodule (ref: https://github.com/cogeotiff/rio-tiler-mosaic/issues/16)

2.0b2 (2020-07-23)
------------------
- add boto3 in the dependency (#201)

2.0b1 (2020-07-22)
------------------
- switch to ContextManager for COG and STAC (rio_cogeo.io.COGReader, rio_cogeo.io.STACReader).
- COGReader.part and STACReader.part return data in BBOX CRS by default.
- STACReader now accept URL (https, s3).
- add more method for STAC (prewiew/point/part/info/stats).
- add expression for COG/STAC preview/point/part.
- add `masked` option in `rio_tiler.reader.point` to control weither or not it should return None or a value.
- remove mission specific tilers (#195).
- remove `rio_tiler.reader.multi_*` functions (replaced by rio_tiler.io.cogeo.multi_*).
- remove `rio_tiler.utils.expression` (replaced by expression options in tilers).

2.0a11 (2020-05-29)
------------------
- refactor `rio_tiler.utils.tile_exists` to allow raster bounds latitude == -90,90

2.0a10 (2020-05-29)
------------------
- Change default resampling to nearest for `_read` (#187)
- add `rio_tiler.reader.stats` (return only array statistics)
- remove default `dst_crs` in `rio_tiler.reader.part` to to fallback to dataset CRS.

2.0a9 (2020-05-27)
------------------
- Refactor colormap and add method to register custom colormap

2.0a8 (2020-05-25)
------------------
- add `preview` method to `rio_tiler.io.cogeo`

2.0a7 (2020-05-17)
------------------
- allow reading high resolution part of a raster (by making height, width args optional)
- add `max_size` option in `rio_tiler.reader.part` to set a maximum output size when height and width are not set
- add point and area function in rio_tiler.io.cogeo
- fix width-height height-widht bug in `rio_tiler.reader.part`

**depreciation**
- deprecated `out_window` option in favor of `window` in rio_tiler.reader._read

2.0a6 (2020-05-06)
------------------
- fix unwanted breacking change with `img_profiles.get` not allowing default values

2.0a5 (2020-05-06)
------------------
- make `rio_tiler.io.landsat8.tile` return Uint16 data and not float32 (#173)
- `rio_tiler.profiles.img_profiles` item access return `copy` of the items (#177)
- better colormap docs (#176, author @kylebarron)

2.0a4 (2020-04-08)
------------------
- add `rio_tiler.io.cogeo.info` to retrieve simple file metadata (no image statistics)
- add band metadata tag info in `rio_tiler.render.metadata` output
- add `rio_tiler.io.stac` STAC compliant rio_tiler.colormap.apply_discrete_cmap

2.0a3 (2020-03-25)
------------------
- only use `transform_bounds` when needed in rio_tiler.reader.part

Breaking Changes:
- switch back to gdal/rasterio calculate_default_transform (#164). Thanks to Terracotta core developper @dionhaefner.
- refactor `rio_tiler.utils.get_vrt_transform` to get width and height input.

2.0a2 (2020-03-20)
------------------
- Fall back to gdal/rasterio calculate_default_transform for dateline separation crossing dataset (ref #164)

2.0a1 (2020-03-19)
------------------
- added `reader.preview`, `reader.point` methods
- added multi_* functions to rio_tiler.reader to support multiple assets addresses
- added `rio_tiler.utils.has_mask_band` function
- added `rio_tiler.utils.get_overview_level` to calculate the overview level needed for partial reading.
- added type hints
- added scale, offsets, colormap, datatype and colorinterp in reader.metadata output (#158)
- new `rio_tiler.colormap` submodule
- added `unscale` options to rio_tiler.reader._read function apply internal scale/offset (#157)

Breaking Changes:
- removed python 2 support
- new package architecture (.io submodule)
- introduced new rio_tiler.reader functions (part, preview, metadata...)
- renamed rio_tiler.main to rio_tiler.io.cogeo
- bucket and prefixes are defined in rio_tiler.io.dataset.`{dataset}_parse` function from
  AWS supported Public Dataset
- renamed `minimum_tile_cover` to `minimum_overlap`
- renamed `tile_edge_padding` to `padding`
- padding is set to 0 by default.
- use terracotta calculate_default_transform (see https://github.com/cogeotiff/rio-tiler/issues/56#issuecomment-442484999)
- colormaps are now have an alpha value
- `rio_tiler.utils.get_colormap` replaced by `rio_tiler.colormap.get_colormap`
- new `rio_tiler.colormap.get_colormap` supports only GDAL like colormap
- replaced `rio_tiler.utils.array_to_image` by `rio_tiler.utils.render`
- replaced `rio_tiler.utils.apply_cmap` by `rio_tiler.colormap.apply_cmap`
- replaced `rio_tiler.utils._apply_discrete_colormap` by `rio_tiler.colormap.apply_discrete_cmap`
- removed `histogram_bins` and `histogram_range` in options in metadata reader.
  Should now be passed in `hist_options` (e.g: hist_options={bins=10, range=(0, 10)})
- remove alpha band value from output data array in tile/preview/metadata #127

1.4.0 (2020-02-19)
------------------
- Add Sentinel2-L2A support (#137)
- Update Sentinel-2 sceneid schema (S2A_tile_20170323_07SNC_0 -> S2A_L1C_20170323_07SNC_0)

1.3.1 (2019-11-06)
------------------
- Add `warp_vrt_option` option for `utils.raster_get_stats` and `utils.tile_read` to
allow more custom VRT Warping. (ref: https://github.com/OSGeo/gdal/issues/1989#issue-518526399)
- Add `rio_tiler.utils.non_alpha_indexes` to find non-alpha band indexes (ref #127)

1.3.0 (2019-10-07)
------------------
- Allow `DatasetReader`, `DatasetWriter`, `WarpedVRT` input for `utils.raster_get_stats` and `utils.tile_read`
- add `minimum_tile_cover` option to filter dataset not covering a certain amount of the tile.
- add Sentinel-1 submodule

Breaking Changes:
- need rasterio>=1.1

1.2.11 (2019-09-18)
-------------------
- reduce memory footprint of expression tiler
- fix wrong calculation for overview size in `raster_get_stats` (#116)
- Add Landsat 8 QA Band (#117).

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
- Add Input (bounds_crs) and Output (dst_crs) option to `utils._tile_read` function (#108)

1.2.7 (2019-05-14)
------------------
- Revert changes introduced in #106 (see #105)
- Refactor tests

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
- return index number with band descriptions (#99)

1.2.2 (2019-04-03)
------------------
- add mercator min/max zoom info in metadata output from rio_tiler.utils.raster_get_stats (#96)
- add band description (band name) in metadata output from rio_tiler.utils.raster_get_stats (#96)

1.2.1 (2019-03-26)
------------------
- Replace rio-pansharpen dependency with a fork of the brovey function directly
into `rio_tiler.utils` (rio-pansharpen is unmaintened and not compatible with
rasterio>=1) (#94).

1.2.0 (2019-03-26)
------------------
- `rio_tiler.utils.array_to_image`'s color_map arg can be a dictionary of discrete values (#91)

Breaking Changes:
- `expr` argument is now a required option in `rio_tiler.utils.expression`. (#88)

1.1.4 (2019-03-11)
------------------
- Add 'rplumbo' colormap (#90 by @DanSchoppe)

1.1.3 (2019-03-06)
------------------
Bug fixes:
- Fix casting to integer for MAX_THREADS environment variable.

1.1.1 (2019-02-21)
------------------
- Minor typo correction and harmonization of the use of src/src_dst/src_path in `rio_tiler.utils`

Bug fixes:
- Fix nodata handling in `utils.raster_get_stats`

1.1.0 (2019-02-15)
------------------
- Allow options forwarding to `tile_read` from `main.tile` function (#86)
- Add `resampling_method` options in `rio_tiler.utils.tile_read` to allow user set
resampling. Default is now bilinear (#85)

Bug fixes:
- Fix nodata option forwarding to tile_read when source is a path (#83)

Refactoring:
- Refactor `rio_tiler.utils.tile_read` to reduce code complexity (#84)

Breaking Changes:
- `indexes` options is now set to **None** in `rio_tiler.utils.tile_read`.
Default will now be the dataset indexes.

1.0.1 (2019-02-14)
------------------
- Fix mask datatype bug in `rio_tiler.utils.array_to_image`(#79)
- Fix nodata handling and better test for the nodata/mask main module (#81)

1.0.0 (2019-02-11)
------------------
- add missing Landsat panchromatic band (08) min/max fetch in `rio_tiler.landsat8.metadata` (#58)
- add pre-commit for commit validation (#64)
- code formatting using Black (the uncompromising Python code formatter) (#64)
- update documentation (Sentinel-2 cost) (#68)
- add `utils.raster_get_stats` and `utils._get_stats` to replace `min_max*` function
and to return more statistics (#66)
- add overview level selection to statistical functions to reduce the data download (#59)
- add pure GDAL `array_to_image` function to replace PIL tools (#29)
- add GDAL format output from `utils.get_colormap` to be used in `array_to_image` (#29)
- add GDAL compatible Image creation profile (#29)
- add max threads number settings via "MAX_THREADS" environment variable (#71)

Breaking Changes:
- update `metadata` structure returned by `landsat8.metadata`, `sentinel2.metadata`, `cbers.metadata`
- force sentinel, landsat and cbers band names to be string and add validation (#65)
- moved landsat utility functions from `rio_tiler.utils` to `rio_tiler.landsat8`
  - rio_tiler.utils.landsat_get_mtl -> rio_tiler.landsat8._landsat_get_mtl
  - rio_tiler.utils.landsat_parse_scene_id -> rio_tiler.landsat8._landsat_parse_scene_id
  - rio_tiler.utils.landsat_get_stats -> rio_tiler.landsat8._landsat_stats
- moved cbers utility functions from `rio_tiler.utils` to `rio_tiler.cbers`
  - rio_tiler.utils.cbers_parse_scene_id -> rio_tiler.cbers._cbers_parse_scene_id
- moved sentinel-2 utility functions from `rio_tiler.utils` to `rio_tiler.sentinel2`
  - rio_tiler.utils.sentinel_parse_scene_id -> rio_tiler.sentinel2._sentinel_parse_scene_id
- removed deprecated PIL support as well as base64 encoding function in rio_tiler.utils
  - rio_tiler.utils.img_to_buffer
  - rio_tiler.utils.array_to_img
  - rio_tiler.utils.b64_encode_img
- removed deprecated min_max* functions (landsat_min_max_worker and band_min_max_worker)

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
- fix mask (internal/external) fetching 🙏
- fix boundless read with new rasterio 1.0b2
- fix custom nodata handling
- fix performances issue

Breaking Changes:
- removed alpha band options to select a custom alpha band number

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
- `utils.tile_band_worker` renamed to `utils.tile_read`
- `main.tile` **rgb** option renamed **indexes**
- `sentinel2.tile`, `landsat8.tile`,  `cbers.tile` **rgb** option renamed **bands**
- `main.tile` default nodata mask is handled by rasterio

1.0a4 (2018-03-07)
------------------
- adds utils.b64_encode_img function to encode an image object into a base64 string
- add tiles profiles (jpeg, png, webp) based on https://github.com/mapnik/mapnik/wiki/Image-IO#default-output-details

Breaking Changes:
- Refactor `rio_tiler.utils.array_to_img` to return PIL image object

1.0a3 (2018-02-05)
------------------
- only using `read_masks` for mask creation when it's needed.

1.0a2 (2018-02-05)
------------------
- add "expression" utility function
- better nodata/mask/alpha band definition and support

Breaking Changes:
- tile functions now return an associated mask (Landsat, Sentinel, CBERS, main)
- remove nodata support in utils.image_to_array function
- add mask support in utils.image_to_array function
- utils.tile_band_worker will always return a (Band, Width, Height) array (e.g 1x256x256 or 3x256x256)

1.0a1 (2018-01-04)
------------------
- remove aws.py sub-module (replaced by main.py)
- no default bands value for main.py tiles.

1.0a.0 (2018-01-03)
------------------
- add colormap option in `utils.array_to_img`
- add TIR (brightness temps) support
- add CBERS support
- add global file support
- add elevation encoding for mapzen
- removing internal caching
- update to rasterio 1.0a12

Breaking Changes:
- remove data value rescaling in `landsat8.tile` and `sentinel2.tile`
- fix wrong lat/grid_square value in `utils.sentinel_parse_scene_id`
- rename `utils.sentinel_min_max_worker` to `utils.band_min_max_worker`

0.0.3 (2017-11-14)
------------------
- Fix Sentinel-2 bad AWS url

0.0.2 (2017-10-17)
------------------
- Fix python 2/3 compatibilities in rio_tiler.utils.landsat_get_mtl

0.0.1 (2017-10-05)
------------------
- Initial release. Requires Rasterio >= 1.0a10.
