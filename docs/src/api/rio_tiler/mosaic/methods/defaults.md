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

    
Add data to tile.

### HighestMethod

```python3
class HighestMethod(
    
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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

    
Add data to tile.

### LastBandHigh

```python3
class LastBandHigh(
    
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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
    tile: numpy.ma.core.MaskedArray
)
```

    
Add data to tile.

### LastBandLow

```python3
class LastBandLow(
    
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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
    tile: numpy.ma.core.MaskedArray
)
```

    
Add data to tile.

### LowestMethod

```python3
class LowestMethod(
    
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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

    
Add data to tile.

### MeanMethod

```python3
class MeanMethod(
    enforce_data_type=True
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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

    
Add data to tile.

### MedianMethod

```python3
class MedianMethod(
    enforce_data_type=True
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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

    
Create a stack of tile.

### StdevMethod

```python3
class StdevMethod(
    enforce_data_type=True
)
```

#### Ancestors (in MRO)

* rio_tiler.mosaic.methods.base.MosaicMethodBase
* abc.ABC

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

    
Add data to tile.