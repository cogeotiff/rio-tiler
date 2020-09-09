"""rio_tiler.io.base: ABC class for rio-tiler readers."""

import abc
import re
import warnings
from typing import Any, Dict, List, Optional, Sequence, Tuple, Type, Union

import attr
import numpy

from ..errors import ExpressionMixingWarning, MissingAssets
from ..expression import apply_expression
from ..tasks import multi_arrays, multi_values


@attr.s
class BaseReader(metaclass=abc.ABCMeta):
    """Rio-tiler.io BaseReader."""

    bounds: Tuple[float, float, float, float] = attr.ib(init=False)
    minzoom: int = attr.ib(init=False)
    maxzoom: int = attr.ib(init=False)

    @abc.abstractmethod
    def __enter__(self):
        """Support using with Context Managers."""
        ...

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        ...

    @property
    def center(self) -> Tuple[float, float, int]:
        """Dataset center + minzoom."""
        return (
            (self.bounds[0] + self.bounds[2]) / 2,
            (self.bounds[1] + self.bounds[3]) / 2,
            self.minzoom,
        )

    @abc.abstractmethod
    def info(self) -> Dict:
        """Return Dataset's info."""
        ...

    @property
    def spatial_info(self) -> Dict:
        """Return Dataset's spatial info."""
        return {
            "bounds": self.bounds,
            "center": self.center,
            "minzoom": self.minzoom,
            "maxzoom": self.maxzoom,
        }

    @abc.abstractmethod
    def stats(self, pmin: float = 2.0, pmax: float = 98.0, **kwargs: Any) -> Dict:
        """Return Dataset's statistics."""
        ...

    @abc.abstractmethod
    def metadata(self, pmin: float = 2.0, pmax: float = 98.0, **kwargs: Any,) -> Dict:
        """Return Dataset's statistics and info."""
        info = self.info()
        info["statistics"] = self.stats(pmin, pmax, **kwargs)
        return info

    @abc.abstractmethod
    def tile(
        self, tile_x: int, tile_y: int, tile_z: int, **kwargs: Any
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Read a Map tile from the Dataset."""
        ...

    @abc.abstractmethod
    def part(
        self, bbox: Tuple[float, float, float, float], **kwargs: Any
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Read a Part of a Dataset."""
        ...

    @abc.abstractmethod
    def preview(self, **kwargs: Any) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Return a preview of a Dataset."""
        ...

    @abc.abstractmethod
    def point(self, lon: float, lat: float, **kwargs: Any) -> List:
        """Read a value from a Dataset."""
        ...


@attr.s
class MultiBaseReader(BaseReader, metaclass=abc.ABCMeta):
    """MultiBaseReader Reader."""

    reader: Type[BaseReader] = attr.ib()
    reader_options: Dict = attr.ib(factory=dict)
    bounds: Tuple[float, float, float, float] = attr.ib(init=False)
    assets: Sequence[str] = attr.ib(init=False)

    @abc.abstractmethod
    def __enter__(self):
        """Support using with Context Managers."""
        ...

    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    @abc.abstractmethod
    def _get_asset_url(self, asset: str) -> str:
        """Validate asset name and construct url."""
        ...

    def parse_expression(self, expression: str) -> Tuple:
        """Parse rio-tiler band math expression."""
        assets = "|".join([fr"\b{asset}\b" for asset in self.assets])
        _re = re.compile(assets.replace("\\\\", "\\"))
        return tuple(set(re.findall(_re, expression)))

    def info(
        self, assets: Union[Sequence[str], str] = None, *args, **kwargs: Any
    ) -> Dict:
        """Return metadata from multiple assets"""
        if not assets:
            raise MissingAssets("Missing 'assets' option")

        if isinstance(assets, str):
            assets = (assets,)

        def _reader(asset: str, **kwargs: Any) -> Dict:
            url = self._get_asset_url(asset)
            with self.reader(url, **self.reader_options) as cog:  # type: ignore
                return cog.info()

        return multi_values(assets, _reader, *args, **kwargs)

    def stats(
        self,
        pmin: float = 2.0,
        pmax: float = 98.0,
        assets: Union[Sequence[str], str] = None,
        **kwargs: Any,
    ) -> Dict:
        """Return array statistics from multiple assets"""
        if not assets:
            raise MissingAssets("Missing 'assets' option")

        if isinstance(assets, str):
            assets = (assets,)

        def _reader(asset: str, *args, **kwargs) -> Dict:
            url = self._get_asset_url(asset)
            with self.reader(url, **self.reader_options) as cog:  # type: ignore
                return cog.stats(*args, **kwargs)

        return multi_values(assets, _reader, pmin, pmax, **kwargs)

    def metadata(
        self,
        pmin: float = 2.0,
        pmax: float = 98.0,
        assets: Union[Sequence[str], str] = None,
        **kwargs: Any,
    ) -> Dict:
        """Return metadata from multiple assets"""
        if not assets:
            raise MissingAssets("Missing 'assets' option")

        if isinstance(assets, str):
            assets = (assets,)

        def _reader(asset: str, *args, **kwargs) -> Dict:
            url = self._get_asset_url(asset)
            with self.reader(url, **self.reader_options) as cog:  # type: ignore
                return cog.metadata(*args, **kwargs)

        return multi_values(assets, _reader, pmin, pmax, **kwargs)

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = "",
        asset_expression: Optional[
            str
        ] = "",  # Expression for each asset based on index names
        **kwargs: Any,
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Read a Mercator Map tile multiple assets."""
        if isinstance(assets, str):
            assets = (assets,)

        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        def _reader(
            asset: str, *args: Any, **kwargs: Any
        ) -> Tuple[numpy.ndarray, numpy.ndarray]:
            url = self._get_asset_url(asset)
            with self.reader(url, **self.reader_options) as cog:  # type: ignore
                return cog.tile(*args, **kwargs)

        data, mask = multi_arrays(
            assets,
            _reader,
            tile_x,
            tile_y,
            tile_z,
            expression=asset_expression,
            **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            data = apply_expression(blocks, assets, data)

        return data, mask

    def part(
        self,
        bbox: Tuple[float, float, float, float],
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = "",
        asset_expression: Optional[
            str
        ] = "",  # Expression for each asset based on index names
        **kwargs: Any,
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Read part of multiple assets."""
        if isinstance(assets, str):
            assets = (assets,)

        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        def _reader(
            asset: str, *args: Any, **kwargs: Any
        ) -> Tuple[numpy.ndarray, numpy.ndarray]:
            url = self._get_asset_url(asset)
            with self.reader(url, **self.reader_options) as cog:  # type: ignore
                return cog.part(*args, **kwargs)

        data, mask = multi_arrays(
            assets, _reader, bbox, expression=asset_expression, **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            data = apply_expression(blocks, assets, data)

        return data, mask

    def preview(
        self,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = "",
        asset_expression: Optional[
            str
        ] = "",  # Expression for each asset based on index names
        **kwargs: Any,
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Return a preview from multiple assets."""
        if isinstance(assets, str):
            assets = (assets,)

        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        def _reader(asset: str, **kwargs: Any) -> Tuple[numpy.ndarray, numpy.ndarray]:
            url = self._get_asset_url(asset)
            with self.reader(url, **self.reader_options) as cog:  # type: ignore
                return cog.preview(**kwargs)

        data, mask = multi_arrays(
            assets, _reader, expression=asset_expression, **kwargs
        )

        if expression:
            blocks = expression.split(",")
            data = apply_expression(blocks, assets, data)

        return data, mask

    def point(
        self,
        lon: float,
        lat: float,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = "",
        asset_expression: Optional[
            str
        ] = "",  # Expression for each asset based on index names
        **kwargs: Any,
    ) -> List:
        """Read a value from COGs."""
        if isinstance(assets, str):
            assets = (assets,)

        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        def _reader(asset: str, *args, **kwargs: Any) -> Dict:
            url = self._get_asset_url(asset)
            with self.reader(url, **self.reader_options) as cog:  # type: ignore
                return cog.point(*args, **kwargs)

        data = multi_values(
            assets, _reader, lon, lat, expression=asset_expression, **kwargs,
        )

        values = [d for _, d in data.items()]
        if expression:
            blocks = expression.split(",")
            values = apply_expression(blocks, assets, values).tolist()

        return values
