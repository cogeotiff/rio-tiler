# Module rio_tiler.mosaic.methods.defaults

rio_tiler.mosaic.methods.defaults: default mosaic filling methods.

None

## Classes

### FirstMethod

```python3
class FirstMethod(
    
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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
    array: Optional[numpy.ma.core.MaskedArray]
)
```

    
Add data to the mosaic array.

### HighestMethod

```python3
class HighestMethod(
    
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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
    array: Optional[numpy.ma.core.MaskedArray]
)
```

    
Add data to the mosaic array.

### LastBandHighMethod

```python3
class LastBandHighMethod(
    
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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
    array: Optional[numpy.ma.core.MaskedArray]
)
```

    
Add data to the mosaic array.

### LastBandLowMethod

```python3
class LastBandLowMethod(
    
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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
    array: Optional[numpy.ma.core.MaskedArray]
)
```

    
Add data to the mosaic array.

### LowestMethod

```python3
class LowestMethod(
    
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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
    array: Optional[numpy.ma.core.MaskedArray]
)
```

    
Add data to the mosaic array.

### MeanMethod

```python3
class MeanMethod(
    enforce_data_type: bool = True
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

#### Class variables

```python3
cutline_mask
```

```python3
enforce_data_type
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

Return Mean of the data stack.

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

    
Add array to the stack.

### MedianMethod

```python3
class MedianMethod(
    enforce_data_type: bool = True
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

#### Class variables

```python3
cutline_mask
```

```python3
enforce_data_type
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

Return Median of the data stack.

```python3
is_done
```

Check if the mosaic filling is done.

#### Methods

    
#### feed

```python3
def feed(
    self,
    array: Optional[numpy.ma.core.MaskedArray]
)
```

    
Add array to the stack.

### StdevMethod

```python3
class StdevMethod(
    
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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

Return STDDEV of the data stack.

```python3
is_done
```

Check if the mosaic filling is done.

#### Methods

    
#### feed

```python3
def feed(
    self,
    array: Optional[numpy.ma.core.MaskedArray]
)
```

    
Add array to the stack.