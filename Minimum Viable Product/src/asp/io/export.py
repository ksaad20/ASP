"""
Export utilities for ASP.

Provides serialization helpers for planning results and
other ASP objects.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class DataExporter:
    """
    Export ASP objects to disk.
    """

    def export(
        self,
        obj: Any,
        path: str | Path,
    ) -> Path:
        """
        Export an object to JSON.

        Parameters
        ----------
        obj:
            Object to export.

        path:
            Destination file.

        Returns
        -------
        pathlib.Path
            Written file path.
        """

        destination = Path(path)
        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with destination.open(
            "w",
            encoding="utf-8",
        ) as handle:
            json.dump(
                self._serialize(obj),
                handle,
                indent=2,
                sort_keys=True,
            )

        return destination

    @classmethod
    def json(
        cls,
        obj: Any,
        path: str | Path,
    ) -> Path:
        """
        Export an object as JSON.

        This convenience method exists for compatibility
        with the ASP CLI.
        """

        return cls().export(
            obj=obj,
            path=path,
        )

    def _serialize(
        self,
        obj: Any,
    ) -> Any:
        """
        Convert an object into JSON-compatible data.
        """

        if hasattr(obj, "to_dict"):
            return obj.to_dict()

        if isinstance(obj, dict):
            return {
                key: self._serialize(value)
                for key, value in obj.items()
            }

        if isinstance(obj, (list, tuple)):
            return [
                self._serialize(item)
                for item in obj
            ]

        if isinstance(
            obj,
            (
                str,
                int,
                float,
                bool,
            ),
        ) or obj is None:
            return obj

        return str(obj)
