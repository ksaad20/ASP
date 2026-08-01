"""
Export utilities for ASP.

Provides serialization of planning results to JSON.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class DataExporter:
    """
    Export planning results and other ASP objects.
    """

    def export(
        self,
        obj: Any,
        path: str | Path,
    ) -> Path:
        """
        Export an object to a JSON file.

        Parameters
        ----------
        obj
            Object to export.

        path
            Destination path.

        Returns
        -------
        pathlib.Path
            Path to the written file.
        """

        destination = Path(path)
        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with destination.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                self._serialize(obj),
                file,
                indent=2,
                sort_keys=True,
            )

        return destination

    def _serialize(
        self,
        obj: Any,
    ) -> Any:
        """
        Convert an object into JSON-serializable data.
        """

        if hasattr(obj, "to_dict"):
            return obj.to_dict()

        if isinstance(
            obj,
            dict,
        ):
            return {
                key: self._serialize(value)
                for key, value in obj.items()
            }

        if isinstance(
            obj,
            (
                list,
                tuple,
            ),
        ):
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
