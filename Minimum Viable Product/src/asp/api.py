"""
Public API for Autonomous Synthesis Planner (ASP).

This module provides the main programmatic interface for
creating planners and generating synthesis routes.
"""

from __future__ import annotations

from asp.planning.planner import Planner


class ASP:
    """
    Main Autonomous Synthesis Planner interface.

    Provides a simple entry point for users who want to
    interact with ASP programmatically.
    """

    def __init__(self) -> None:
        """
        Initialize ASP.
        """

        self.template_count: int = 0


    def planner(self, target: str) -> Planner:
        """
        Create a synthesis planner for a target molecule.

        Parameters
        ----------
        target:
            Target molecule representation, such as SMILES.

        Returns
        -------
        Planner
            Configured synthesis planner.
        """

        return Planner(target)


def plan(target: str) -> Planner:
    planner = Planner()
    planner.target = target
    return planner
