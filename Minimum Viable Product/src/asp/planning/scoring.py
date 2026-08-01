"""
Route scoring for Autonomous Synthesis Planner.

This module defines the scoring framework used to evaluate and rank
candidate retrosynthetic routes. The MVP implements a deterministic,
weighted scoring model designed to be simple, interpretable, and easily
extensible.

Future versions may incorporate reaction databases, synthetic
accessibility metrics, cost estimation, machine learning models,
and multi-objective optimization.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from asp.chemistry import Reaction


@dataclass(slots=True)
class Route:
    """
    Represents a candidate synthesis route.

    Parameters
    ----------
    reactions
        Ordered sequence of reactions.

    score
        Overall route score.
    """

    reactions: list[Reaction] = field(default_factory=list)

    score: float = 0.0

    @property
    def steps(self) -> int:
        """Return the number of reaction steps."""
        return len(self.reactions)

    @property
    def average_confidence(self) -> float:
        """Average reaction confidence."""
        if not self.reactions:
            return 0.0

        return (
            sum(r.confidence for r in self.reactions)
            / len(self.reactions)
        )

    def add_reaction(
        self,
        reaction: Reaction,
    ) -> None:
        """Append a reaction to the route."""
        self.reactions.append(reaction)

    def to_dict(self) -> dict:
        """Serialize the route."""
        return {
            "score": self.score,
            "steps": self.steps,
            "average_confidence": self.average_confidence,
            "reactions": [
                r.to_dict()
                for r in self.reactions
            ],
        }


@dataclass(slots=True)
class RouteScorer:
    """
    Scores candidate synthesis routes.
    """

    complexity_weight: float = 1.0

    confidence_weight: float = 1.0

    step_weight: float = 1.0

    def score(
        self,
        route: Route,
    ) -> float:
        """
        Compute a weighted route score.

        Higher scores indicate more favorable routes.
        """

        confidence = route.average_confidence

        complexity = 1.0 / max(route.steps, 1)

        step_score = 1.0 / max(route.steps, 1)

        score = (
            self.confidence_weight * confidence
            + self.complexity_weight * complexity
            + self.step_weight * step_score
        )

        route.score = score

        return score

    def rank(
        self,
        routes: list[Route],
    ) -> list[Route]:
        """
        Rank candidate routes from best to worst.
        """

        for route in routes:
            self.score(route)

        return sorted(
            routes,
            key=lambda route: route.score,
            reverse=True,
        )

    def best(
        self,
        routes: list[Route],
    ) -> Route | None:
        """
        Return the highest-scoring route.
        """

        ranked = self.rank(routes)

        if not ranked:
            return None

        return ranked[0]
