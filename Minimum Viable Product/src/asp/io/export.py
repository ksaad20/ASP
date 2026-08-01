"""
Export utilities for ASP.
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
        result: Any,
        path: str | Path,
    ) -> Path:
        """
        Export a planning result.

        Parameters
        ----------
        result:
            Object to export.

        path:
            Output file.

        Returns
        -------
        Path
            Output path.
        """

        output = Path(path)
        output.parent.mkdir(parents=True, exist_ok=True)

        if hasattr(result, "to_dict"):
            data = result.to_dict()
        elif hasattr(result, "__dict__"):
            data = result.__dict__
        else:
            raise TypeError(
                f"Unsupported export type: {type(result).__name__}",
            )

        output.write_text(
            json.dumps(
                data,
                indent=2,
                default=str,
            ),
            encoding="utf-8",
        )

        return output

    def export_json(
        self,
        result: Any,
        path: str | Path,
    ) -> Path:
        """
        Export as JSON.

        This is an alias for ``export``.
        """

        return self.export(result, path)
