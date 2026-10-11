# Experimental Features

In this section you will find documentation for new, experimental features in rio-tiler. These features are subject to change or removal, and we are looking for feedback and suggestions before making them a permanent part of Pydantic.


## Feedback

We welcome feedback on experimental features! Please open an issue on the [rio-tiler GitHub repository](https://github.com/cogeotiff/rio-tiler/issues/new/choose) to share your thoughts, requests, or suggestions.

We also encourage you to read through existing feedback and add your thoughts to existing issues.

## Warnings on Import

When you import an experimental feature from the `experimental` module, you'll see a warning message that the feature is experimental. You can disable this warning with the following:

```python
import warnings
from rio_tiler.errors import RioTilerExperimentalWarning

warnings.filterwarnings('ignore', category=RioTilerExperimentalWarning)
```