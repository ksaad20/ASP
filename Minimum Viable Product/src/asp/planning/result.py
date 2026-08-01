"""
Planning result models for ASP.

Defines the objects returned by the retrosynthesis engine and the
high-level Planner interface.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .route import Route
from .search import SearchTree


@dataclass(slots=True)
class PlanningResult:
    """
    Result produced by a planning run.
    """

    target: Any
    routes: list[Route] = field(default_factory=list)
    search_tree: SearchTree = field(default_factory=SearchTree)
    expanded_nodes: int = 0
    generated_routes: int = 0
    elapsed_time: float = 0.0

    @property
    def route_count(self) -> int:
        """
        Return the number of generated routes.
        """

        return len(self.routes)

    @property
    def best_route(self) -> Route | None:
        """
        Return the highest-scoring route.
        """

        if not self.routes:
            return None

        return max(
            self.routes,
            key=lambda route: route.score,
        )

    @property
    def successful(self) -> bool:
        """
        Whether at least one route was found.
        """

        return bool(self.routes)

    def add_route(
        self,
        route: Route,
    ) -> None:
        """
        Add a route to the result.
        """

        self.routes.append(route)

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the planning result.
        """

        return {
            "target": getattr(
                self.target,
                "to_dict",
                lambda: self.target,
            )(),
            "routes": [
                route.to_dict()
                for route in self.routes
            ],
            "expanded_nodes": self.expanded_nodes,
            "generated_routes": self.generated_routes,
            "elapsed_time": self.elapsed_time,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "PlanningResult":
        """
        Construct a PlanningResult from a dictionary.
        """

        routes = [
            Route.from_dict(route)
            for route in data.get("routes", [])
        ]

        return cls(
            target=data.get("target"),
            routes=routes,
            expanded_nodes=int(
                data.get(
                    "expanded_nodes",
                    0,
                ),
            ),
            generated_routes=int(
                data.get(
                    "generated_routes",
                    0,
                ),
            ),
            elapsed_time=float(
                data.get(
                    "elapsed_time",
                    0.0,
                ),
            ),
        )

    def __len__(self) -> int:
        """
        Return the number of routes.
        """

        return len(self.routes)

    def __bool__(self) -> bool:
        """
        Return whether planning succeeded.
        """

        return self.successful

    def __repr__(self) -> str:
        """
        Return a concise representation.
        """

        return (
            "PlanningResult("
            f"routes={self.route_count}, "
            f"expanded_nodes={self.expanded_nodes}, "
            f"generated_routes={self.generated_routes})"
        )
