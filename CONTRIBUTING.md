# Contributing

Issues and pull requests are more than welcome.

**dev install**

```bash
$ git clone https://github.com/cogeotiff/rio-tiler.git
$ cd rio-tiler
$ pip install -e .[dev]
```

**Python3.7 only**

This repo is set to use `pre-commit` to run *isort*, *flake8*, *pydocstring*, *black* ("uncompromising Python code formatter") and mypy when committing new code.

```bash
$ pre-commit install
```

### Docs

```bash
$ git clone https://github.com/cogeotiff/rio-tiler.git
$ cd rio-tiler
$ pip install -e .["docs"]
```

Hot-reloading docs:

```bash
$ mkdocs serve
```

To manually deploy docs (note you should never need to do this because Github
Actions deploys automatically for new commits.):

```bash
$ mkdocs gh-deploy
```

```bash
pdocs as_markdown \
   --output_dir docs/api/ \
   --exclude_source \
   --overwrite \
   rio_tiler.colormap \
   rio_tiler.constants \
   rio_tiler.errors \
   rio_tiler.expression \
   rio_tiler.models \
   rio_tiler.io.base \
   rio_tiler.io.cogeo \
   rio_tiler.io.stac \
   rio_tiler.mosaic.methods.base \
   rio_tiler.mosaic.methods.defaults \
   rio_tiler.mosaic.reader \
   rio_tiler.profiles \
   rio_tiler.reader \
   rio_tiler.tasks \
   rio_tiler.utils
```
