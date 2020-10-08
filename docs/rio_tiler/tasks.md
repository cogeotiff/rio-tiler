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

```python3
logger
```

## Functions

    
### create_tasks

```python3
def create_tasks(
    reader: Callable,
    assets,
    threads,
    *args,
    **kwargs
) -> Union[Generator[Tuple[Callable, str], NoneType, NoneType], Sequence[Tuple[concurrent.futures._base.Future, str]]]
```

    
Create Future Tasks.

    
### filter_tasks

```python3
def filter_tasks(
    tasks: Union[Generator[Tuple[Callable, str], NoneType, NoneType], Sequence[Tuple[concurrent.futures._base.Future, str]]],
    allowed_exceptions: Union[Tuple, NoneType] = None
) -> Generator
```

    
Filter tasks to remove Exceptions.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tasks | list or generator | Sequence of 'concurrent.futures._base.Future' or 'callable' | None |
| allowed_exceptions | Tuple | List of exceptions which won't be raised. | None |

**Yields:**

| Type | Description |
|---|---|
| Successful task's result | None |

    
### multi_arrays

```python3
def multi_arrays(
    assets: Sequence[str],
    reader: Callable,
    *args: Any,
    threads: int = 80,
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Multi array.

    
### multi_values

```python3
def multi_values(
    assets: Sequence[str],
    reader: Callable,
    *args: Any,
    threads: int = 80,
    **kwargs: Any
) -> Dict
```

    
Multi Values.