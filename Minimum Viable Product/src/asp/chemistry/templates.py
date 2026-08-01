"""
Reaction template representation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .reaction import Reaction


@dataclass(slots=True)
class ReactionTemplate:
    """
    Representation of a reusable reaction template.
    """

    reaction: Reaction | None = None
    identifier: str = "unnamed"
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_reaction(
        cls,
        reaction: Reaction,
        *,
        identifier: str = "unnamed",
        **metadata: Any,
    ) -> "ReactionTemplate":
        """
        Construct a template from a reaction.
        """

        return cls(
            reaction=reaction,
            identifier=identifier,
            metadata=metadata,
        )

    @property
    def reaction_smiles(self) -> str:
        """
        Return the underlying reaction SMILES.
        """

        if self.reaction is None:
            return ""

        return self.reaction.reaction_smiles

    def matches(
        self,
        reaction: Reaction,
    ) -> bool:
        """
        Determine whether a reaction matches this template.
        """

        if self.reaction is None:
            return False

        return (
            self.reaction.reaction_smiles
            == reaction.reaction_smiles
        )

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the template.
        """

        return {
            "identifier": self.identifier,
            "reaction": (
                self.reaction.to_dict()
                if self.reaction is not None
                else None
            ),
            "metadata": self.metadata,
        }
