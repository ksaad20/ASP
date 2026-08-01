"""
Retrosynthesis engine for Autonomous Synthesis Planner.

The RetrosynthesisEngine is responsible for generating candidate synthesis
routes for a target molecule using a collection of reaction templates.

The MVP implements a deterministic template-based search framework that is
intentionally simple while providing a clean architecture for future
beam search, A*, Monte Carlo Tree Search, and machine learning-guided
planning algorithms.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from asp.chemistry import Molecule, ReactionTemplate

from .route import Route
from .search import SearchNode, SearchTree


@dataclass(slots=True)
class PlanningResult:
    """
    Result returned by the retrosynthesis engine.
    """

    target: Molecule

    routes: list[Route] = field(default_factory=list)

    search_tree: SearchTree | None = None

    expanded_nodes: int = 0

    generated_routes: int = 0

    elapsed_time: float = 0.0

    @property
    def best_route(self) -> Route | None:
        """
        Return the highest-scoring route.

        Routes are expected to be ranked before this
        property is accessed.
        """
        if not self.routes:
            return None

        return self.routes[0]

    def add_route(
        self,
        route: Route,
    ) -> None:
        """
        Add a candidate synthesis route.
        """
        self.routes.append(route)

    def __len__(self) -> int:
        return len(self.routes)


class RetrosynthesisEngine:
    """
    Template-based retrosynthesis engine.
    """

    def __init__(
        self,
        templates: list[ReactionTemplate] | None = None,
        *,
        max_depth: int = 5,
    ) -> None:

        self.templates = templates or []

        self.max_depth = max_depth

    def plan(
        self,
        target: Molecule,
    ) -> PlanningResult:
        """
        Generate candidate synthesis routes.

        Parameters
        ----------
        target
            Target molecule.

        Returns
        -------
        PlanningResult
        """

        tree = SearchTree(target)

        result = PlanningResult(
            target=target,
            search_tree=tree,
        )

        self._expand(
            node=tree.root,
            route=Route(target=target),
            result=result,
        )

        return result

    def _expand(
        self,
        *,
        node: SearchNode,
        route: Route,
        result: PlanningResult,
    ) -> None:
        """
        Recursively expand a search node.
        """

        if node.depth >= self.max_depth:
            result.add_route(route.copy())
            return

        node.expanded = True

        result.expanded_nodes += 1

        matching_templates = self._match_templates(
            node.molecule
        )

        if not matching_templates:
            result.add_route(route.copy())
            return

        for template in matching_templates:

            child_route = route.copy()

            child_route.add_reaction(
                template.reaction
            )

            child = SearchNode(
                molecule=node.molecule,
                depth=node.depth + 1,
            )

            node.add_child(child)

            self._expand(
                node=child,
                route=child_route,
                result=result,
            )

        result.generated_routes = len(result.routes)

    def _match_templates(
        self,
        molecule: Molecule,
    ) -> list[ReactionTemplate]:
        """
        Find reaction templates applicable to a molecule.

        MVP implementation:

        Returns every enabled template.

        Future versions will perform
        reaction SMARTS matching,
        graph matching,
        fingerprint similarity,
        neural template ranking,
        and reaction feasibility prediction.
        """

        del molecule

        return [
            template
            for template in self.templates
            if template.enabled
        ]
