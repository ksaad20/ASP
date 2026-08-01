"""
Route domain model for Autonomous Synthesis Planner.

A Route represents a complete candidate synthesis pathway from available
starting materials to a target molecule.

The Route class is intentionally independent of the scoring and search
algorithms so that it can be reused throughout the planning engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from asp.chemistry import Molecule, Reaction


@dataclass(slots=True)
class Route:
    """
    Represents a candidate synthesis route.

    Parameters
    ----------
    target
        Target molecule.

    reactions
        Ordered sequence of reactions.

    score
        Overall route score.

    metadata
        Optional user metadata.
    """

    target: Molecule

    reactions: list[Reaction] = field(default_factory=list)

    score: float = 0.0

    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def steps(self) -> int:
        """Return the number of reaction steps."""
        return len(self.reactions)

    @property
    def reactants(self) -> list[Molecule]:
        """
        Return all reactant molecules.
        """
        molecules: list[Molecule] = []

        for reaction in self.reactions:
            molecules.extend(reaction.reactants)

        return molecules

    @property
    def products(self) -> list[Molecule]:
        """
        Return all product molecules.
        """
        molecules: list[Molecule] = []

        for reaction in self.reactions:
            molecules.extend(reaction.products)

        return molecules

    @property
    def average_confidence(self) -> float:
        """
        Average reaction confidence.
        """
        if not self.reactions:
            return 0.0

        return (
            sum(
                reaction.confidence
                for reaction in self.reactions
            )
            / len(self.reactions)
        )

    def add_reaction(
        self,
        reaction: Reaction,
    ) -> None:
        """
        Append a reaction to the route.
        """
        self.reactions.append(reaction)

    def extend(
        self,
        reactions: list[Reaction],
    ) -> None:
        """
        Append multiple reactions.
        """
        self.reactions.extend(reactions)

    def copy(self) -> "Route":
        """
        Return a shallow copy of the route.
        """
        return Route(
            target=self.target,
            reactions=list(self.reactions),
            score=self.score,
            metadata=dict(self.metadata),
        )

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the route.
        """
        return {
            "target": self.target.to_dict(),
            "steps": self.steps,
            "score": self.score,
            "average_confidence": self.average_confidence,
            "reactions": [
                reaction.to_dict()
                for reaction in self.reactions
            ],
            "metadata": self.metadata,
        }

    def __len__(self) -> int:
        return self.steps

    def __iter__(self):
        return iter(self.reactions)

    def __repr__(self) -> str:
        return (
            "Route("
            f"target={self.target!s}, "
            f"steps={self.steps}, "
            f"score={self.score:.3f})"
        )
