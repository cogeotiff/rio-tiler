# Plan: Expression Security Hardening

Co-Authored-By: Claude Sonnet 4.6 noreply@anthropic.com

## TL;DR

Replace the fragile denylist in `validate_expression` with an AST allowlist, after a security researcher demonstrated that the original `"eval("` string check is trivially bypassed using `exec()`, `compile()`, and other Python builtins.

## Background

A security researcher reported that a cloud provider had applied a similar `"eval("` string check and it was bypassed using `exec()` and `compile()`. The original code in [expression.py](rio_tiler/expression.py) had two weak defenses:

1. A string check: `if "eval(" in expr` — bypassed by `exec(...)`, `compile(...)`, `getattr(__builtins__, 'eval')(...)`, etc.
2. An AST blocklist for `ast.GeneratorExp` and `ast.SetComp` — blocked two specific node types while allowing everything else.

**Why the actual RCE risk was low (but still wrong):** Expressions are passed to `numexpr.evaluate()`, not Python's `eval()`. numexpr has its own VM that doesn't know about `exec`, `compile`, or `__import__`. However, the denylist gives false confidence and would be dangerous if `validate_expression` were ever reused in a context that called Python's `eval()`.

## What Changed

### [rio_tiler/expression.py](rio_tiler/expression.py)

**Removed:**
- String check `if "eval(" in expr`

**Added:**
- `_ALLOWED_NODES` — explicit tuple of permitted AST node types (arithmetic ops, comparisons, constants, name references, allowed calls, and their operator/context nodes)
- `_ALLOWED_FUNCTIONS` — imported directly from `numexpr.expressions.functions`, so the allowlist stays automatically in sync with what numexpr actually supports
- `validate_expression` now iterates over `;`-separated blocks (via `get_expression_blocks`) and validates each one independently

**Bypass vectors now blocked:**

| Expression | Caught by |
|---|---|
| `exec(...)` | `exec` not in numexpr's functions dict |
| `compile(...)` | same |
| `__import__('os').system(...)` | `ast.Attribute` not in `_ALLOWED_NODES` |
| `getattr(...)('eval')(...)` | `func` is a `Call`, not a `Name` → indirect call check |
| `b1.__class__` | `ast.Attribute` not in `_ALLOWED_NODES` |
| `lambda: b1` | `ast.Lambda` not in `_ALLOWED_NODES` |
| `[x for x in ...]` | `ast.ListComp` not in `_ALLOWED_NODES` |
| `open('/etc/passwd')` | `open` not in numexpr's functions dict |
| `b1[0]` | `ast.Subscript` not in `_ALLOWED_NODES` |

### [tests/test_expression.py](tests/test_expression.py)

- Expanded `test_parse_eval_invalid` (renamed from `test_parse_eval_error`) with concrete bypass attempts covering `exec`, `compile`, attribute access, lambdas, comprehensions, arbitrary function calls, and subscript access
- Expanded `test_parse_eval_valid` with cases covering all operator types and the full set of numexpr math functions (`sin`, `cos`, `log`, `sqrt`, `where`, `sum`, `round`, etc.)
