# Module rio_tiler.mosaic.methods.base

rio-tiler.mosaic.methods abc class.

## Classes

### MosaicMethodBase

```python3
class MosaicMethodBase(
    
)
```

Abstract base class for rio-tiler-mosaic methods objects.

#### Ancestors (in MRO)

* abc.ABC

#### Descendants

* rio_tiler.mosaic.methods.defaults.FirstMethod
* rio_tiler.mosaic.methods.defaults.HighestMethod
* rio_tiler.mosaic.methods.defaults.LowestMethod
* rio_tiler.mosaic.methods.defaults.MeanMethod
* rio_tiler.mosaic.methods.defaults.MedianMethod
* rio_tiler.mosaic.methods.defaults.StdevMethod
* rio_tiler.mosaic.methods.defaults.LastBandHighMethod
* rio_tiler.mosaic.methods.defaults.LastBandLowMethod
* rio_tiler.mosaic.methods.defaults.CountMethod

#### Class variables

```python3
cutline_mask
```

```python3
exit_when_filled
```

```python3
mosaic
```

#### Instance variables

```python3
data
```

Return data.

```python3
is_done
```

Check if the mosaic filling is done.

#### Methods

    
#### feed

```python3
def feed(
    self,
    array: numpy.ma.core.MaskedArray
)
```

Fill mosaic array.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| array | numpy.ma.ndarray | data | None |