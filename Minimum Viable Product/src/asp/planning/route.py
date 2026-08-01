"""
Route representation for ASP.

Defines a retrosynthetic route consisting of a target molecule,
a sequence of reaction steps, and an optional score.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Route:
    """
    Representation of a retrosynthetic route.
    """

    target: Any
    steps: list[Any] = field(default_factory=list)
    score: float = 0.0

    @property
    def reaction_count(self) -> int:
        """
        Return the number of reactions in the route.
        """

        return len(self.steps)

    def add_step(
        self,
        step: Any,
    ) -> None:
        """
        Add a planning step to the route.
        """

        self.steps.append(step)

    def add_reaction(
        self,
        reaction: Any,
    ) -> None:
        """
        Add a reaction to the route.

        This method is maintained for backwards compatibility
        with the scoring and visualization modules.
        """

        self.add_step(reaction)

    def clear(self) -> None:
        """
        Remove all reaction steps.
        """

        self.steps.clear()

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the route.
        """

        return {
            "target": (
                self.target.to_dict()
                if hasattr(self.target, "to_dict")
                else self.target
            ),
            "steps": [
                step.to_dict()
                if hasattr(step, "to_dict")
                else step
                for step in self.steps
            ],
            "reaction_count": self.reaction_count,
            "score": self.score,
        }

    def __len__(self) -> int:
        """
        Return the number of reaction steps.
        """

        return len(self.steps)

    def __iter__(self):
        """
        Iterate over reaction steps.
        """

        return iter(self.steps)

    def __repr__(self) -> str:
        """
        Return a developer-friendly representation.
        """

        return (
            f"Route("
            f"target={self.target!r}, "
            f"steps={len(self.steps)}, "
            f"score={self.score:.3f}"
            f")"
        )
