"""
Planning result container.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .route import Route
from .search import SearchTree


@dataclass(slots=True)
class PlanningResult:
    """
    Result returned by the planner.
    """

    target: Any
    routes: list[Route] = field(default_factory=list)
    search_tree: SearchTree | None = None
    expanded_nodes: int = 0
    generated_routes: int = 0
    elapsed_time: float = 0.0

    def __len__(self) -> int:
        """
        Return the number of routes.
        """

        return len(self.routes)

    def __iter__(self):
        """
        Iterate over routes.
        """

        return iter(self.routes)

    @property
    def route_count(self) -> int:
        """
        Number of routes.
        """

        return len(self.routes)

    @property
    def best_route(self) -> Route | None:
        """
        Return the highest-scoring route.
        """

        if not self.routes:
            return None

        return max(self.routes, key=lambda route: route.score)

    def add_route(
        self,
        route: Route,
    ) -> None:
        """
        Add a route to the result.
        """

        self.routes.append(route)
        self.generated_routes = len(self.routes)

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the planning result.
        """

        return {
            "target": (
                self.target.to_dict()
                if hasattr(self.target, "to_dict")
                else str(self.target)
            ),
            "routes": [
                route.to_dict()
                if hasattr(route, "to_dict")
                else str(route)
                for route in self.routes
            ],
            "expanded_nodes": self.expanded_nodes,
            "generated_routes": self.generated_routes,
            "elapsed_time": self.elapsed_time,
        }
