"""
Public API for Autonomous Synthesis Planner (ASP).

This module provides the main programmatic interface for
creating planners and generating synthesis routes.
"""

from __future__ import annotations

from pathlib import Path

from asp.io.export import DataExporter
from asp.planning.planner import Planner
from asp.planning.result import PlanningResult


class ASP:
    """
    Main Autonomous Synthesis Planner interface.
    """

    def __init__(self) -> None:
        """Initialize ASP."""

        self.template_count = 0

    def plan(self, target: str) -> PlanningResult:
        """
        Generate a synthesis plan for a target molecule.
        """

        planner = Planner()
        return planner.plan(target)

    def load_templates(self, path: Path | str) -> None:
        """
        Load synthesis templates.
        """

        _ = Path(path)
        self.template_count += 1

    def export(
        self,
        result: PlanningResult,
        path: Path | str,
    ) -> object:
        """
        Export a planning result.
        """

        exporter = DataExporter()
        return exporter.export(result, path)


def plan(target: str) -> PlanningResult:
    """
    Convenience function for generating a synthesis plan.
    """

    return ASP().plan(target)
