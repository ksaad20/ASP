"""
High-level planning interface for Autonomous Synthesis Planner.

This module exposes the primary public API used by applications,
scripts, notebooks, and the command-line interface.

Example
-------
>>> from asp import Planner
>>> planner = Planner()
>>> result = planner.plan("CCO")
"""

from __future__ import annotations

from pathlib import Path

from asp.chemistry import Molecule, MoleculeParser, ReactionTemplate

from .retrosynthesis import PlanningResult, RetrosynthesisEngine
from .scoring import RouteScorer


class Planner:
    """
    High-level synthesis planner.

    The Planner coordinates molecular parsing, retrosynthetic planning,
    and route ranking behind a single, easy-to-use interface.
    """

    def __init__(
        self,
        *,
        templates: list[ReactionTemplate] | None = None,
        max_depth: int = 5,
        beam_width: int = 10,
        max_routes: int = 20,
    ) -> None:
        """
        Initialize a planner instance.
        """

        self.engine = RetrosynthesisEngine(
            templates=templates,
            max_depth=max_depth,
        )

        self.scorer = RouteScorer()

        self.max_routes = max_routes
        self.beam_width = beam_width

    def plan(
        self,
        target: str | Molecule,
    ) -> PlanningResult:
        """
        Generate synthesis routes for a target molecule.

        Parameters
        ----------
        target
            Either a SMILES string or a Molecule instance.

        Returns
        -------
        PlanningResult
        """

        molecule = self._parse_target(target)

        result = self.engine.plan(molecule)

        result.routes = self.scorer.rank(
            result.routes
        )[: self.max_routes]

        return result

    def load_templates(
        self,
        templates: list[ReactionTemplate],
    ) -> None:
        """
        Replace the current reaction template library.
        """

        self.engine.templates = templates

    def add_template(
        self,
        template: ReactionTemplate,
    ) -> None:
        """
        Register a new reaction template.
        """

        self.engine.templates.append(template)

    def clear_templates(self) -> None:
        """
        Remove every reaction template.
        """

        self.engine.templates.clear()

    @property
    def template_count(self) -> int:
        """
        Number of registered templates.
        """

        return len(self.engine.templates)

    @staticmethod
    def _parse_target(
        target: str | Molecule,
    ) -> Molecule:
        """
        Convert user input into a Molecule object.
        """

        if isinstance(target, Molecule):
            return target

        return MoleculeParser.from_smiles(target)

    @classmethod
    def from_template_file(
        cls,
        path: str | Path,
    ) -> "Planner":
        """
        Construct a planner from a template file.

        Placeholder implementation for the MVP.
        """

        del path

        return cls()

    def __repr__(self) -> str:
        return (
            "Planner("
            f"templates={self.template_count}, "
            f"max_routes={self.max_routes}"
            ")"
        )
