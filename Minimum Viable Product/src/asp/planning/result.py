```python
"""
Planning result models for Autonomous Synthesis Planner.

This module defines the PlanningResult object returned by the planning
engine and exposed through the public Planner API.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator

from .route import Route
from .search import SearchTree


@dataclass(slots=True)
class PlanningStatistics:
    """
    Planning execution statistics.
    """

    expanded_nodes: int = 0
    generated_routes: int = 0
    evaluated_routes: int = 0
    search_depth: int = 0
    elapsed_time: float = 0.0


@dataclass(slots=True)
class PlanningResult:
    """
    Result returned by the planning engine.

    Parameters
    ----------
    routes
        Ranked candidate synthesis routes.

    search_tree
        Search tree generated during planning.

    statistics
        Planning execution statistics.
    """

    routes: list[Route] = field(default_factory=list)

    search_tree: SearchTree | None = None

    statistics: PlanningStatistics = field(
        default_factory=PlanningStatistics
    )

    @property
    def best_route(self) -> Route | None:
        """
        Highest-ranked synthesis route.
        """
        if not self.routes:
            return None

        return self.routes[0]

    @property
    def route_count(self) -> int:
        """
        Number of candidate routes.
        """
        return len(self.routes)

    @property
    def successful(self) -> bool:
        """
        True if at least one route was generated.
        """
        return self.route_count > 0

    def add_route(
        self,
        route: Route,
    ) -> None:
        """
        Add a candidate route.
        """
        self.routes.append(route)

    def extend(
        self,
        routes: list[Route],
    ) -> None:
        """
        Append multiple routes.
        """
        self.routes.extend(routes)

    def sort(
        self,
        *,
        reverse: bool = True,
    ) -> None:
        """
        Sort routes by score.
        """
        self.routes.sort(
            key=lambda route: route.score,
            reverse=reverse,
        )

    def to_dict(self) -> dict:
        """
        Serialize the planning result.
        """
        return {
            "route_count": self.route_count,
            "successful": self.successful,
            "statistics": {
                "expanded_nodes":
                    self.statistics.expanded_nodes,
                "generated_routes":
                    self.statistics.generated_routes,
                "evaluated_routes":
                    self.statistics.evaluated_routes,
                "search_depth":
                    self.statistics.search_depth,
                "elapsed_time":
                    self.statistics.elapsed_time,
            },
            "routes": [
                route.to_dict()
                for route in self.routes
            ],
        }

    def __len__(self) -> int:
        return self.route_count

    def __iter__(self) -> Iterator[Route]:
        return iter(self.routes)

    def __getitem__(
        self,
        index: int,
    ) -> Route:
        return self.routes[index]

    def __bool__(self) -> bool:
        return self.successful

    def __repr__(self) -> str:
        return (
            "PlanningResult("
            f"routes={self.route_count}, "
            f"successful={self.successful})"
        )
```

