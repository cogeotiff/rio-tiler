# Module rio_tiler.errors

Errors and warnings.

## Classes

### AlphaBandWarning

```python3
class AlphaBandWarning(
    /,
    *args,
    **kwargs
)
```

Automatically removed Alpha band from output array.

#### Ancestors (in MRO)

* builtins.UserWarning
* builtins.Warning
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### AssetAsBandError

```python3
class AssetAsBandError(
    /,
    *args,
    **kwargs
)
```

Can't use asset_as_band with multiple bands.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### ColorMapAlreadyRegistered

```python3
class ColorMapAlreadyRegistered(
    /,
    *args,
    **kwargs
)
```

ColorMap is already registered.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### EmptyMosaicError

```python3
class EmptyMosaicError(
    /,
    *args,
    **kwargs
)
```

Mosaic method returned empty array.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### ExpressionMixingWarning

```python3
class ExpressionMixingWarning(
    /,
    *args,
    **kwargs
)
```

Expression and assets/indexes mixing.

#### Ancestors (in MRO)

* builtins.UserWarning
* builtins.Warning
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### InvalidAssetName

```python3
class InvalidAssetName(
    /,
    *args,
    **kwargs
)
```

Invalid Asset name.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### InvalidBandName

```python3
class InvalidBandName(
    /,
    *args,
    **kwargs
)
```

Invalid band name.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### InvalidBufferSize

```python3
class InvalidBufferSize(
    /,
    *args,
    **kwargs
)
```

`buffer` must be a multiple of `0.5` (e.g: 0.5, 1, 1.5, ...).

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### InvalidColorFormat

```python3
class InvalidColorFormat(
    /,
    *args,
    **kwargs
)
```

Invalid color format.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### InvalidColorMapName

```python3
class InvalidColorMapName(
    /,
    *args,
    **kwargs
)
```

Invalid colormap name.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### InvalidDatatypeWarning

```python3
class InvalidDatatypeWarning(
    /,
    *args,
    **kwargs
)
```

Invalid Output Datatype.

#### Ancestors (in MRO)

* builtins.UserWarning
* builtins.Warning
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### InvalidExpression

```python3
class InvalidExpression(
    /,
    *args,
    **kwargs
)
```

Invalid Expression.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### InvalidFormat

```python3
class InvalidFormat(
    /,
    *args,
    **kwargs
)
```

Invalid image format.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### InvalidMosaicMethod

```python3
class InvalidMosaicMethod(
    /,
    *args,
    **kwargs
)
```

Invalid Pixel Selection method for mosaic.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### InvalidPointDataError

```python3
class InvalidPointDataError(
    /,
    *args,
    **kwargs
)
```

Invalid PointData.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### MissingAssets

```python3
class MissingAssets(
    /,
    *args,
    **kwargs
)
```

Missing Assets.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### MissingBands

```python3
class MissingBands(
    /,
    *args,
    **kwargs
)
```

Missing bands.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### NoOverviewWarning

```python3
class NoOverviewWarning(
    /,
    *args,
    **kwargs
)
```

Dataset has no overviews.

#### Ancestors (in MRO)

* builtins.UserWarning
* builtins.Warning
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### PointOutsideBounds

```python3
class PointOutsideBounds(
    /,
    *args,
    **kwargs
)
```

Point is outside image bounds.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### RioTilerError

```python3
class RioTilerError(
    /,
    *args,
    **kwargs
)
```

Base exception class.

#### Ancestors (in MRO)

* builtins.Exception
* builtins.BaseException

#### Descendants

* rio_tiler.errors.InvalidFormat
* rio_tiler.errors.TileOutsideBounds
* rio_tiler.errors.InvalidBufferSize
* rio_tiler.errors.PointOutsideBounds
* rio_tiler.errors.InvalidBandName
* rio_tiler.errors.InvalidColorMapName
* rio_tiler.errors.InvalidAssetName
* rio_tiler.errors.InvalidExpression
* rio_tiler.errors.MissingAssets
* rio_tiler.errors.MissingBands
* rio_tiler.errors.InvalidMosaicMethod
* rio_tiler.errors.ColorMapAlreadyRegistered
* rio_tiler.errors.EmptyMosaicError
* rio_tiler.errors.InvalidColorFormat
* rio_tiler.errors.AssetAsBandError
* rio_tiler.errors.InvalidPointDataError

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.

### TileOutsideBounds

```python3
class TileOutsideBounds(
    /,
    *args,
    **kwargs
)
```

Z-X-Y Tile is outside image bounds.

#### Ancestors (in MRO)

* rio_tiler.errors.RioTilerError
* builtins.Exception
* builtins.BaseException

#### Class variables

```python3
args
```

#### Methods

    
#### with_traceback

```python3
def with_traceback(
    ...
)
```

Exception.with_traceback(tb) --

set self.__traceback__ to tb and return self.