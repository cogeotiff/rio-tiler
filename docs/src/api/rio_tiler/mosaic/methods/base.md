# Module rio_tiler.mosaic.methods.base

rio-tiler.mosaic.methods abc class.

None

## Classes

### MosaicMethodBase

```python3
class MosaicMethodBase(
    
)
```

#### Ancestors (in MRO)

* abc.ABC

#### Descendants

* rio_tiler.mosaic.methods.defaults.FirstMethod
* rio_tiler.mosaic.methods.defaults.HighestMethod
* rio_tiler.mosaic.methods.defaults.LowestMethod
* rio_tiler.mosaic.methods.defaults.MeanMethod
* rio_tiler.mosaic.methods.defaults.MedianMethod
* rio_tiler.mosaic.methods.defaults.StdevMethod
* rio_tiler.mosaic.methods.defaults.LastBandHigh
* rio_tiler.mosaic.methods.defaults.LastBandLow

#### Instance variables

```python3
data
```

Return data and mask.

```python3
is_done
```

Check if the tile filling is done.

#### Methods

    
#### feed

```python3
def feed(
    self,
    tile
)
```

    
Fill mosaic tile.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile | numpy.ma.ndarray | data | None |