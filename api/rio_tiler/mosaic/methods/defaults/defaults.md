# Module rio_tiler.mosaic.methods.defaults

rio_tiler.mosaic.methods.defaults: default mosaic filling methods.

## Classes

### CountMethod

```python3
class CountMethod(
    
)
```

Stack the arrays and return the valid pixel count.

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

Return valid data count of the data stack.

```python3
is_done
```

Check if the mosaic filling is done.

#### Methods

    
#### feed

```python3
def feed(
    self,
    array: Union[numpy.ma.core.MaskedArray, NoneType]
)
```

Add array to the stack.

### FirstMethod

```python3
class FirstMethod(
    
)
```

Feed the mosaic array with the first pixel available.

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
    array: Union[numpy.ma.core.MaskedArray, NoneType]
)
```

Add data to the mosaic array.

### HighestMethod

```python3
class HighestMethod(
    
)
```

Feed the mosaic array with the highest pixel values.

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
    array: Union[numpy.ma.core.MaskedArray, NoneType]
)
```

Add data to the mosaic array.

### LastBandHighMethod

```python3
class LastBandHighMethod(
    
)
```

Feed the mosaic array using the last band as decision factor (highest value).

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
    array: Union[numpy.ma.core.MaskedArray, NoneType]
)
```

Add data to the mosaic array.

### LastBandLowMethod

```python3
class LastBandLowMethod(
    
)
```

Feed the mosaic array using the last band as decision factor (lowest value).

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
    array: Union[numpy.ma.core.MaskedArray, NoneType]
)
```

Add data to the mosaic array.

### LowestMethod

```python3
class LowestMethod(
    
)
```

Feed the mosaic array with the lowest pixel values.

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
    array: Union[numpy.ma.core.MaskedArray, NoneType]
)
```

Add data to the mosaic array.

### MeanMethod

```python3
class MeanMethod(
    enforce_data_type: bool = True
)
```

Stack the arrays and return the Mean pixel value.

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

Stack the arrays and return the Median pixel value.

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
    array: Union[numpy.ma.core.MaskedArray, NoneType]
)
```

Add array to the stack.

### StdevMethod

```python3
class StdevMethod(
    
)
```

Stack the arrays and return the Standard Deviation value.

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
    array: Union[numpy.ma.core.MaskedArray, NoneType]
)
```

Add array to the stack.