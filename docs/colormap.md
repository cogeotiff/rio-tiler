# Colormaps

Rio-tiler includes many colormaps, some derived from Matplotlib and some custom
ones that are commonly used with raster data.

You can load a colormap with `rio_tiler.colormap.get_colormap`, and then pass it
to `rio_tiler.utils.render`:

```python
from rio_tiler.colormap import cmap
from rio_tiler.io import COGReader

with COGReader(
  "s3://landsat-pds/c1/L8/015/029/LC08_L1GT_015029_20200119_20200119_01_RT/LC08_L1GT_015029_20200119_20200119_01_RT_B8.TIF",
  nodata=0,
) as cog:
    img = cog.tile(150, 187, 9)

    # Rescale the data linearly from 0-10000 to 0-255
    image_rescale = img.post_process(in_range=(0, 10000), out_range=(0, 255))

    # Get Colormap
    cm = cmap.get("cfastie")

    # Apply colormap and create a PNG buffer
    buff = image_rescale.render(colormap=cm) # this returns a buffer (PNG by default)
```

![](img/custom.png)
![](img/perceptually_uniform_sequential.png)
![](img/sequential.png)
![](img/sequential_(2).png)
![](img/diverging.png)
![](img/cyclic.png)
![](img/qualitative.png)
![](img/miscellaneous.png)

### References

- Matplotlib colormaps: <https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html>
- `cfastie`: <http://publiclab.org/notes/cfastie/08-26-2014/new-ndvi-colormap>
- `rplumbo`: <https://github.com/cogeotiff/rio-tiler/pull/90>
- `schwarzwald`: <http://soliton.vm.bytemark.co.uk/pub/cpt-city/wkp/schwarzwald/tn/wiki-schwarzwald-cont.png.index.html>

### Update images for new colormaps

To regenerate these images for new colormaps, update the list of colormaps at
the top of `scripts/colormap_thumb.py` and then run

```bash
python scripts/colormap_thumb.py
```
