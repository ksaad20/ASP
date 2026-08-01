from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .reaction import Reaction


@dataclass(slots=True)
class ReactionTemplate:
    """
    Representation of a reusable reaction template.
    """

    identifier: str
    reaction: Reaction
    name: str = "Unnamed Template"
    category: str = "general"
    description: str = ""
    priority: int = 0
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate template fields."""

        if not self.identifier.strip():
            raise ValueError("identifier cannot be empty.")

        if not self.name.strip():
            raise ValueError("name cannot be empty.")

        if self.priority < 0:
            raise ValueError("priority must be non-negative.")

    @classmethod
    def from_reaction(
        cls,
        reaction: Reaction,
        identifier: str = "unnamed",
        **kwargs: Any,
    ) -> ReactionTemplate:
        """
        Create a template from a reaction.
        """

        return cls(
            identifier=identifier,
            reaction=reaction,
            metadata=kwargs,
        )

    @property
    def reaction_smiles(self) -> str:
        """Return the reaction SMILES."""

        return self.reaction.reaction_smiles

    def matches(self, reaction: Reaction) -> bool:
        """
        Determine whether a reaction matches this template.
        """

        return (
            self.reaction.reaction_smiles
            == reaction.reaction_smiles
        )

    def enable(self) -> None:
        """Enable the template."""

        self.enabled = True

    def disable(self) -> None:
        """Disable the template."""

        self.enabled = False

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the template.
        """

        return {
            "identifier": self.identifier,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "priority": self.priority,
            "enabled": self.enabled,
            "reaction": self.reaction.to_dict(),
            "metadata": self.metadata,
    }
