"""
Route representation for ASP.
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
    reactions: list[Any] = field(default_factory=list)
    score: float = 0.0

    @property
    def steps(self) -> int:
        """
        Return the number of reaction steps.
        """

        return len(self.reactions)

    @property
    def reaction_count(self) -> int:
        """
        Return the number of reactions.
        """

        return len(self.reactions)

    @property
    def average_confidence(self) -> float:
        """
        Return the average reaction confidence.
        """

        if not self.reactions:
            return 0.0

        return (
            sum(
                getattr(
                    reaction,
                    "confidence",
                    0.0,
                )
                for reaction in self.reactions
            )
            / len(self.reactions)
        )

    def add_reaction(
        self,
        reaction: Any,
    ) -> None:
        """
        Add a reaction to the route.
        """

        self.reactions.append(reaction)

    def add_step(
        self,
        reaction: Any,
    ) -> None:
        """
        Compatibility alias.
        """

        self.add_reaction(reaction)

    def clear(self) -> None:
        """
        Remove all reactions.
        """

        self.reactions.clear()

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
            "reactions": [
                reaction.to_dict()
                if hasattr(reaction, "to_dict")
                else reaction
                for reaction in self.reactions
            ],
            "steps": self.steps,
            "average_confidence": self.average_confidence,
            "score": self.score,
        }

    def __len__(self) -> int:
        """
        Return the number of reactions.
        """

        return len(self.reactions)

    def __iter__(self):
        """
        Iterate over reactions.
        """

        return iter(self.reactions)

    def __repr__(self) -> str:
        """
        Return a developer-friendly representation.
        """

        return (
            "Route("
            f"target={self.target!r}, "
            f"steps={self.steps}, "
            f"score={self.score:.3f}"
            ")"
    )
