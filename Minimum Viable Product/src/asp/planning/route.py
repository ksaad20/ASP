"""
Route representation for ASP.

Defines retrosynthetic routes, reaction steps,
scoring metadata, and serialization utilities.
"""

from __future__ import annotations

from typing import Any


class Route:
    """
    Representation of a retrosynthetic route.
    """

    def __init__(
        self,
        target: Any,
        steps: list[Any] | None = None,
        reactions: list[Any] | None = None,
        score: float = 0.0,
    ) -> None:
        """
        Initialize a route.

        Parameters
        ----------
        target:
            Target molecule.
        steps:
            Backwards-compatible reaction list argument.
        reactions:
            Reaction list.
        score:
            Route score.
        """

        self.target = target

        if reactions is not None:
            self.reactions = list(reactions)
        elif steps is not None:
            self.reactions = list(steps)
        else:
            self.reactions = []

        self.score = score

    @property
    def steps(self) -> int:
        """
        Return number of reactions in the route.
        """

        return len(self.reactions)

    @property
    def reaction_count(self) -> int:
        """
        Return number of reactions.
        """

        return len(self.reactions)

    @property
    def average_confidence(self) -> float:
        """
        Calculate average reaction confidence.
        """

        if not self.reactions:
            return 0.0

        return sum(
            getattr(
                reaction,
                "confidence",
                0.0,
            )
            for reaction in self.reactions
        ) / len(self.reactions)

    def add_reaction(
        self,
        reaction: Any,
    ) -> None:
        """
        Add a reaction step.
        """

        self.reactions.append(reaction)

    def add_step(
        self,
        step: Any,
    ) -> None:
        """
        Alias for add_reaction.
        """

        self.add_reaction(step)

    def clear(self) -> None:
        """
        Remove all reactions.
        """

        self.reactions.clear()

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize route.
        """

        return {
            "target": (
                self.target.to_dict()
                if hasattr(self.target, "to_dict")
                else self.target
            ),
            "steps": self.steps,
            "reactions": [
                reaction.to_dict()
                if hasattr(reaction, "to_dict")
                else reaction
                for reaction in self.reactions
            ],
            "score": self.score,
            "average_confidence": self.average_confidence,
        }

    def __len__(self) -> int:
        """
        Return number of reactions.
        """

        return len(self.reactions)

    def __iter__(self):
        """
        Iterate over reactions.
        """

        return iter(self.reactions)

    def __repr__(self) -> str:
        """
        Developer representation.
        """

        return (
            "Route("
            f"target={self.target!r}, "
            f"steps={self.steps}, "
            f"score={self.score:.3f}"
            ")"
        )
