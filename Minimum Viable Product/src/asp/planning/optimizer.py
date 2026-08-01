"""
Route optimization for Autonomous Synthesis Planner.

This module defines the RouteOptimizer responsible for refining and
filtering candidate synthesis routes after retrosynthetic search and
before presentation to the user.

The MVP implementation performs deterministic optimization while
providing extension points for future optimization strategies.
"""

from __future__ import annotations

from dataclasses import dataclass

from .route import Route


@dataclass(slots=True)
class RouteOptimizer:
    """
    Optimize candidate synthesis routes.

    Parameters
    ----------
    remove_duplicates
        Remove duplicate routes.

    sort_descending
        Sort routes by score.

    minimum_score
        Discard routes below this score.
    """

    remove_duplicates: bool = True

    sort_descending: bool = True

    minimum_score: float = 0.0

    def optimize(
        self,
        routes: list[Route],
    ) -> list[Route]:
        """
        Optimize a collection of candidate routes.
        """

        optimized = list(routes)

        if self.remove_duplicates:
            optimized = self._remove_duplicates(
                optimized
            )

        optimized = self._filter(
            optimized
        )

        optimized.sort(
            key=lambda route: route.score,
            reverse=self.sort_descending,
        )

        return optimized

    def _remove_duplicates(
        self,
        routes: list[Route],
    ) -> list[Route]:
        """
        Remove duplicate routes.

        Routes are considered identical if they
        contain the same ordered reaction sequence.
        """

        unique: dict[
            tuple[str, ...],
            Route,
        ] = {}

        for route in routes:

            signature = tuple(
                reaction.reaction_smiles
                for reaction in route
            )

            if signature not in unique:
                unique[signature] = route

        return list(unique.values())

    def _filter(
        self,
        routes: list[Route],
    ) -> list[Route]:
        """
        Remove low-quality routes.
        """

        return [
            route
            for route in routes
            if route.score >= self.minimum_score
        ]

    def optimize_route(
        self,
        route: Route,
    ) -> Route:
        """
        Optimize a single route.

        Reserved for future work including:

        * reagent optimization
        * yield estimation
        * route compression
        * cost optimization
        * green chemistry metrics
        * laboratory constraints

        The MVP returns the route unchanged.
        """

        return route

    def __call__(
        self,
        routes: list[Route],
    ) -> list[Route]:
        """
        Callable interface.
        """

        return self.optimize(routes)
