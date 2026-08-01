"""
Reaction template definitions for ASP.

Reaction templates encapsulate reusable transformations that may be
applied during retrosynthetic planning.
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
    name: str = "Unnamed Template"
    category: str = "general"
    description: str = ""
    priority: int = 0
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate template fields.
        """

        self.identifier = self.identifier.strip()
        self.name = self.name.strip()
        self.category = self.category.strip()

        if not self.identifier:
            raise ValueError("identifier cannot be empty.")

        if not self.name:
            raise ValueError("name cannot be empty.")

        if self.priority < 0:
            raise ValueError("priority must be non-negative.")

    @classmethod
    def from_reaction(
        cls,
        reaction: Reaction,
        *,
        identifier: str = "unnamed",
        name: str | None = None,
        category: str = "general",
        description: str = "",
        priority: int = 0,
        enabled: bool = True,
        **metadata: Any,
    ) -> ReactionTemplate:
        """
        Construct a template from a reaction.
        """

        return cls(
            reaction=reaction,
            identifier=identifier,
            name=name or identifier,
            category=category,
            description=description,
            priority=priority,
            enabled=enabled,
            metadata=metadata,
        )

    @property
    def reaction_smiles(self) -> str:
        """
        Return the reaction SMILES.
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

    def enable(self) -> None:
        """
        Enable the template.
        """

        self.enabled = True

    def disable(self) -> None:
        """
        Disable the template.
        """

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
            "reaction": (
                self.reaction.to_dict()
                if self.reaction is not None
                else None
            ),
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> ReactionTemplate:
        """
        Construct a template from a dictionary.
        """

        reaction_data = data.get("reaction")

        reaction = (
            Reaction.from_dict(reaction_data)
            if reaction_data is not None
            else None
        )

        return cls(
            reaction=reaction,
            identifier=data.get("identifier", "unnamed"),
            name=data.get("name", "Unnamed Template"),
            category=data.get("category", "general"),
            description=data.get("description", ""),
            priority=int(data.get("priority", 0)),
            enabled=bool(data.get("enabled", True)),
            metadata=dict(data.get("metadata", {})),
        )

    def __repr__(self) -> str:
        """
        Return a concise string representation.
        """

        return (
            f"ReactionTemplate("
            f"identifier={self.identifier!r}, "
            f"enabled={self.enabled}, "
            f"priority={self.priority})"
        )
