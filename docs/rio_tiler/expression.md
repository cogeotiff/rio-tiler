# Module rio_tiler.expression

rio-tiler.expression: Parse and Apply expression.

None

## Functions

    
### apply_expression

```python3
def apply_expression(
    blocks: Sequence[str],
    bands: Sequence[Union[str, int]],
    data: numpy.ndarray
) -> numpy.ndarray
```

    
Apply rio-tiler expression.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| blocks | Tuple or List | expression for a specific layer. | None |
| bands | Tuple or List | bands names. | None |
| data | numpy.array | array of bands. | None |

**Returns:**

| Type | Description |
|---|---|
| numpy.array | None |

    
### parse_expression

```python3
def parse_expression(
    expression: str,
    cast: bool = True
) -> Tuple
```

    
Parse rio-tiler band math expression.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| expression | str | band math/combination expression (e.g b3/b2). | None |

**Returns:**

| Type | Description |
|---|---|
| Tuple | None |