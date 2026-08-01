"""
Public API for Autonomous Synthesis Planner (ASP).

This module provides the main programmatic interface for
creating planners and generating synthesis routes.
"""

from __future__ import annotations

from pathlib import Path

from asp.planning.planner import Planner


class ASP:
    """
    Main Autonomous Synthesis Planner interface.

    Provides a simple entry point for users who want to
    interact with ASP programmatically.
    """

    def __init__(self) -> None:
        """Initialize ASP."""

        self.template_count: int = 0

    def plan(self, target: str) -> Planner:
        """
        Create a synthesis planner for a target molecule.

        Parameters
        ----------
        target:
            Target molecule representation.

        Returns
        -------
        Planner
            Configured synthesis planner.
        """

        planner = Planner()
        planner.target = target
        return planner

    def load_templates(self, path: Path | str) -> None:
        """
        Load synthesis templates.

        Parameters
        ----------
        path:
            Path to the template file.
        """

        _ = Path(path)
        self.template_count += 1


def plan(target: str) -> Planner:
    """
    Create a synthesis planner.

    Parameters
    ----------
    target:
        Target molecule representation.

    Returns
    -------
    Planner
        Configured synthesis planner.
    """

    planner = Planner()
    planner.target = target
    return planner.plan(target)

def export(self, result: object, path: Path | str) -> object:
    """
    Export a planning result.

    Parameters
    ----------
    result:
        Planning result to export.

    path:
        Output file path.

    Returns
    -------
    object
        Export result from the exporter.
    """

    from asp.io.export import DataExporter

    exporter = DataExporter()
    return exporter.export(result, path)
