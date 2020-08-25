# Contributing

## Create documentation

```
pip install mkdocs mkdocs-material pygments pdocs
```

Create API documentation:

```bash
pdocs as_markdown \
    --output_dir docs/ \
    --template_dir docs/pdocs_templates \
    --exclude_source \
    --overwrite \
    rio_tiler.colormap \
    rio_tiler.constants \
    rio_tiler.errors \
    rio_tiler.expression \
    rio_tiler.io.base \
    rio_tiler.io.cogeo \
    rio_tiler.io.stac \
    rio_tiler.mercator \
    rio_tiler.mosaic.methods.base \
    rio_tiler.mosaic.methods.defaults \
    rio_tiler.mosaic.reader \
    rio_tiler.profiles \
    rio_tiler.reader \
    rio_tiler.tasks \
    rio_tiler.utils
```

Serve website with hot reloading (hot reloading doesn't apply to API docs):

```
mkdocs serve
```

Deploy to Github Pages:

```
mkdocs gh-deploy
```
