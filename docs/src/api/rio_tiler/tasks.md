# Module rio_tiler.tasks

rio_tiler.tasks: tools for handling rio-tiler's future tasks.

None

## Variables

```python3
MAX_THREADS
```

```python3
TaskType
```

## Functions

    
### create_tasks

```python3
def create_tasks(
    reader: Callable,
    asset_list: Sequence,
    threads: int,
    *args,
    **kwargs
) -> Sequence[Tuple[Union[concurrent.futures._base.Future, Callable], Any]]
```

    
Create Future Tasks.

    
### filter_tasks

```python3
def filter_tasks(
    tasks: Sequence[Tuple[Union[concurrent.futures._base.Future, Callable], Any]],
    allowed_exceptions: Optional[Tuple] = None
) -> Generator
```

    
Filter Tasks to remove Exceptions.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tasks | sequence | Sequence of 'concurrent.futures._base.Future' or 'Callable' | None |
| allowed_exceptions | tuple | List of exceptions which won't be raised. | None |

**Yields:**

| Type | Description |
|---|---|
| None | Task results. |

    
### multi_arrays

```python3
def multi_arrays(
    asset_list: Sequence,
    reader: Callable[..., rio_tiler.models.ImageData],
    *args: Any,
    threads: int = 40,
    allowed_exceptions: Optional[Tuple] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Merge arrays returned from tasks.

    
### multi_points

```python3
def multi_points(
    asset_list: Sequence,
    reader: Callable[..., rio_tiler.models.PointData],
    *args: Any,
    threads: int = 40,
    allowed_exceptions: Optional[Tuple] = None,
    **kwargs: Any
) -> rio_tiler.models.PointData
```

    
Merge points returned from tasks.

    
### multi_values

```python3
def multi_values(
    asset_list: Sequence,
    reader: Callable,
    *args: Any,
    threads: int = 40,
    allowed_exceptions: Optional[Tuple] = None,
    **kwargs: Any
) -> Dict
```

    
Merge values returned from tasks.