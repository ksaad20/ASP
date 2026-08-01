"""
Planner interface for the Autonomous Synthesis Planner (ASP).

Provides the primary user-facing planning API.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from asp.chemistry import (
    MoleculeParser,
    ParsedMolecule,
    ReactionTemplate,
)

from .result import PlanningResult
from .retrosynthesis import RetrosynthesisEngine


class Planner:
    """
    High-level synthesis planner.
    """

    def __init__(
        self,
        *,
        templates: list[ReactionTemplate] | None = None,
        max_routes: int = 20,
    ) -> None:
        """
        Initialize the planner.
        """

        self.templates: list[ReactionTemplate] = templates or []
        self.max_routes = max_routes

    @property
    def template_count(self) -> int:
        """
        Number of registered templates.
        """

        return len(self.templates)

    def add_template(
        self,
        template: ReactionTemplate,
    ) -> None:
        """
        Register a template.
        """

        self.templates.append(template)

    def load_templates(
        self,
        _: Path | str,
    ) -> None:
        """
        Placeholder template loader for the MVP.
        """

        return

    def clear_templates(self) -> None:
        """
        Remove all registered templates.
        """

        self.templates.clear()

    def plan(
        self,
        target: str | ParsedMolecule,
    ) -> PlanningResult:
        """
        Plan a retrosynthetic route.
        """

        if isinstance(target, str):
            molecule = MoleculeParser.from_smiles(target)
        else:
            molecule = target

        engine = RetrosynthesisEngine(
            templates=self.templates,
            max_routes=self.max_routes,
        )

        return engine.plan(molecule)

    def __call__(
        self,
        target: str | ParsedMolecule,
    ) -> PlanningResult:
        """
        Convenience wrapper.
        """

        return self.plan(target)

    def __len__(self) -> int:
        """
        Number of loaded templates.
        """

        return self.template_count

    def __repr__(self) -> str:
        """
        Planner representation.
        """

        return (
            "Planner("
            f"templates={self.template_count}, "
            f"max_routes={self.max_routes})"
        )
