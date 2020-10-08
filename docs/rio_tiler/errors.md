# Module rio_tiler.errors

Errors and warnings.

None

## Classes

### AlphaBandWarning

```python3
class AlphaBandWarning(
    /,
    *args,
    **kwargs
)
```

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

### ColorMapAlreadyRegistered

```python3
class ColorMapAlreadyRegistered(
    /,
    *args,
    **kwargs
)
```

#### Ancestors (in MRO)

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

### DeprecationWarning

```python3
class DeprecationWarning(
    /,
    *args,
    **kwargs
)
```

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

### ExpressionMixingWarning

```python3
class ExpressionMixingWarning(
    /,
    *args,
    **kwargs
)
```

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

#### Ancestors (in MRO)

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

#### Ancestors (in MRO)

* builtins.Exception
* builtins.BaseException

#### Descendants

* rio_tiler.errors.InvalidFormat
* rio_tiler.errors.TileOutsideBounds
* rio_tiler.errors.PointOutsideBounds
* rio_tiler.errors.InvalidBandName
* rio_tiler.errors.InvalidAssetName
* rio_tiler.errors.MissingAssets
* rio_tiler.errors.MissingBands
* rio_tiler.errors.InvalidMosaicMethod

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