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
| blocks | sequence | expression for a specific layer. | None |
| bands | sequence | bands names. | None |
| data | numpy.array |  array of bands. | None |

**Returns:**

| Type | Description |
|---|---|
| numpy.array | output data. |

    
### get_expression_blocks

```python3
def get_expression_blocks(
    expression: str
) -> List[str]
```

    
Split expression in blocks.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| expression | str | band math/combination expression. | None |

**Returns:**

| Type | Description |
|---|---|
| list | expression blocks (str). |

    
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
| expression | str | band math/combination expression. | None |
| cast | bool | cast band names to integers (convert to index values). Defaults to True. | True |

**Returns:**

| Type | Description |
|---|---|
| tuple | band names/indexes. |