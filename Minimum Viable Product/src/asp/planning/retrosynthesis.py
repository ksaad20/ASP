"""
Retrosynthesis engine for ASP.

This module implements the minimum viable retrosynthetic search
engine used by the high-level Planner API.
"""

from __future__ import annotations

from time import perf_counter

from asp.chemistry import (
    MoleculeParser,
    ParsedMolecule,
    ReactionTemplate,
)

from .result import PlanningResult
from .route import Route
from .search import SearchNode, SearchTree


class RetrosynthesisEngine:
    """
    Minimal retrosynthesis engine.
    """

    def __init__(
        self,
        *,
        templates: list[ReactionTemplate] | None = None,
        max_depth: int = 5,
        max_routes: int = 20,
    ) -> None:
        """
        Initialize the retrosynthesis engine.
        """

        self.templates: list[ReactionTemplate] = templates or []
        self.max_depth = max_depth
        self.max_routes = max_routes

    @property
    def template_count(self) -> int:
        """
        Return the number of loaded templates.
        """

        return len(self.templates)

    def add_template(
        self,
        template: ReactionTemplate,
    ) -> None:
        """
        Register a reaction template.
        """

        self.templates.append(template)

    def clear_templates(self) -> None:
        """
        Remove all loaded templates.
        """

        self.templates.clear()

    def plan(
        self,
        target: str | ParsedMolecule,
    ) -> PlanningResult:
        """
        Perform retrosynthetic planning.
        """

        start = perf_counter()

        if isinstance(target, str):
            target = MoleculeParser.from_smiles(target)

        root = SearchNode(
            molecule=target,
        )

        tree = SearchTree(
            root=root,
        )

        route = Route(
            target=target,
            steps=[],
            score=1.0,
        )

        generated_routes = sum(
            1
            for template in self.templates
            if template.enabled
        )

        result = PlanningResult(
            target=target,
            routes=[route],
            search_tree=tree,
            expanded_nodes=1,
            generated_routes=generated_routes,
            elapsed_time=perf_counter() - start,
        )

        return result

    def __call__(
        self,
        target: str | ParsedMolecule,
    ) -> PlanningResult:
        """
        Execute planning.
        """

        return self.plan(target)

    def __repr__(self) -> str:
        """
        Return a string representation.
        """

        return (
            "RetrosynthesisEngine("
            f"templates={self.template_count}, "
            f"max_depth={self.max_depth}, "
            f"max_routes={self.max_routes})"
        )
