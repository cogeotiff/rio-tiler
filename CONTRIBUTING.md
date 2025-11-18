# Contributing

Issues and pull requests are more than welcome.

We recommand using [`uv`](https://docs.astral.sh/uv) as project manager for development.

See https://docs.astral.sh/uv/getting-started/installation/ for installation 

### dev install

```bash
git clone https://github.com/cogeotiff/rio-tiler.git
cd rio-tiler

uv sync
```

You can then run the tests with the following command:

```sh
uv run pytest --cov rio_tiler --cov-report term-missing
```

##### Performance tests

```sh
uv run --group performance pytest tests/benchmarks/benchmarks.py --benchmark-only --benchmark-columns 'min, max, mean, median' --benchmark-sort 'min'
```

### pre-commit

This repo is set to use `pre-commit` to run *isort*, *flake8*, *pydocstring*, *black* ("uncompromising Python code formatter") and mypy when committing new code.

```bash
uv run pre-commit install
```

### Docs

```bash
git clone https://github.com/cogeotiff/rio-tiler.git
cd rio-tiler
```

Hot-reloading docs:

```bash
uv run --group docs mkdocs serve -f docs/mkdocs.yml
```

To manually deploy docs (note you should never need to do this because Github
Actions deploys automatically for new commits.):

```bash
uv run --group docs mkdocs gh-deploy -f docs/mkdocs.yml
```