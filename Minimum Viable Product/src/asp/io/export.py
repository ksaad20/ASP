"""
Data export utilities for Autonomous Synthesis Planner.

This module provides serialization and export functionality for ASP
domain objects. It supports writing molecules, reactions, synthesis
routes, and planning results to common interchange formats.

The MVP focuses on JSON export while providing extension points for
CSV, YAML, SDF, GraphML, PDF reports, and visualization exports.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from asp.chemistry import Molecule, Reaction, ReactionTemplate
from asp.planning.result import PlanningResult
from asp.planning.route import Route


class DataExporter:
    """
    High-level exporter for ASP objects.
    """

    @staticmethod
    def molecule(
        molecule: Molecule,
    ) -> dict[str, Any]:
        """
        Serialize a Molecule.
        """
        return molecule.to_dict()

    @staticmethod
    def reaction(
        reaction: Reaction,
    ) -> dict[str, Any]:
        """
        Serialize a Reaction.
        """
        return reaction.to_dict()

    @staticmethod
    def template(
        template: ReactionTemplate,
    ) -> dict[str, Any]:
        """
        Serialize a ReactionTemplate.
        """
        return template.to_dict()

    @staticmethod
    def route(
        route: Route,
    ) -> dict[str, Any]:
        """
        Serialize a synthesis route.
        """
        return route.to_dict()

    @staticmethod
    def result(
        result: PlanningResult,
    ) -> dict[str, Any]:
        """
        Serialize a planning result.
        """
        return result.to_dict()

    @classmethod
    def json(
        cls,
        obj: Any,
        path: str | Path,
        *,
        indent: int = 4,
    ) -> None:
        """
        Export an ASP object to JSON.
        """

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if hasattr(obj, "to_dict"):
            payload = obj.to_dict()
        elif isinstance(obj, dict):
            payload = obj
        else:
            raise TypeError(
                f"Unsupported export type: "
                f"{type(obj).__name__}"
            )

        with path.open(
            "w",
            encoding="utf-8",
        ) as handle:
            json.dump(
                payload,
                handle,
                indent=indent,
                sort_keys=True,
            )

    @staticmethod
    def supported_formats() -> tuple[str, ...]:
        """
        Return supported export formats.
        """
        return (
            "json",
        )

    @staticmethod
    def supports(
        format_name: str,
    ) -> bool:
        """
        Check whether an export format is supported.
        """
        return (
            format_name.lower()
            in DataExporter.supported_formats()
        )
