"""
Core planner implementation.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from asp.chemistry import MoleculeParser, ParsedMolecule, ReactionTemplate

from .result import PlanningResult
from .route import Route
from .search import SearchTree


class Planner:
    """
    Autonomous synthesis planner.
    """

    def __init__(
        self,
        *,
        max_routes: int = 20,
    ) -> None:
        """
        Initialize the planner.
        """

        self.max_routes = max_routes
        self.templates: list[ReactionTemplate] = []
        self.target: ParsedMolecule | None = None

    def add_template(
        self,
        template: ReactionTemplate,
    ) -> None:
        """
        Register a reaction template.
        """

        self.templates.append(template)

    def load_templates(
        self,
        path: str | Path,
    ) -> None:
        """
        Load templates from disk.

        MVP placeholder implementation.
        """

        _ = Path(path)

    def plan(
        self,
        target: str | ParsedMolecule,
    ) -> PlanningResult:
        """
        Generate synthesis routes.
        """

        if isinstance(target, ParsedMolecule):
            molecule = target
        else:
            molecule = MoleculeParser.from_smiles(target)

        self.target = molecule

        route = Route(target=molecule)
        search_tree = SearchTree()

        result = PlanningResult(
            target=molecule,
            routes=[route],
            search_tree=search_tree,
            expanded_nodes=1,
            generated_routes=1,
            elapsed_time=0.0,
        )

        return result

    @classmethod
    def from_file(
        cls,
        path: str | Path,
    ) -> "Planner":
        """
        Construct a planner from a template file.
        """

        planner = cls()
        planner.load_templates(path)
        return planner

    def __len__(self) -> int:
        """
        Return the number of loaded templates.
        """

        return len(self.templates)

    def __repr__(self) -> str:
        """
        Return a representation of the planner.
        """

        return (
            f"Planner("
            f"templates={len(self.templates)}, "
            f"max_routes={self.max_routes}"
            f")"
        )
