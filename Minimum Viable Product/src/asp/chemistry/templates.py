"""
Reaction template definitions for Autonomous Synthesis Planner.

This module provides the ReactionTemplate class, which encapsulates reusable
reaction transformation rules used by the retrosynthesis engine.

In the MVP, templates are lightweight metadata objects. Future versions can
extend them to support SMARTS-based reaction transformations, learned reaction
templates, and template prioritization.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .reaction import Reaction


@dataclass(slots=True)
class ReactionTemplate:
    """
    Represents a reusable reaction template.

    Parameters
    ----------
    identifier
        Unique template identifier.

    name
        Human-readable template name.

    reaction
        Representative reaction implementing the transformation.

    category
        Reaction category (e.g. oxidation, reduction).

    description
        Optional description.

    priority
        Relative template priority.

    enabled
        Whether the template is active.

    metadata
        Additional user-defined metadata.
    """

    identifier: str

    name: str

    reaction: Reaction

    category: str = "general"

    description: str = ""

    priority: int = 100

    enabled: bool = True

    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate template fields."""

        if not self.identifier.strip():
            raise ValueError(
                "identifier cannot be empty."
            )

        if not self.name.strip():
            raise ValueError(
                "name cannot be empty."
            )

        if self.priority < 0:
            raise ValueError(
                "priority must be non-negative."
            )

    @property
    def reaction_smiles(self) -> str:
        """Return the template reaction as reaction SMILES."""
        return self.reaction.reaction_smiles

    def matches(
        self,
        reaction: Reaction,
    ) -> bool:
        """
        Determine whether a reaction matches this template.

        The MVP performs a simple reaction-SMILES comparison.
        Future implementations may use reaction SMARTS,
        graph isomorphism, fingerprints, or machine learning.
        """
        return (
            self.reaction.reaction_smiles ==
            reaction.reaction_smiles
        )

    def enable(self) -> None:
        """Enable the template."""
        self.enabled = True

    def disable(self) -> None:
        """Disable the template."""
        self.enabled = False

    def to_dict(self) -> dict[str, Any]:
        """Serialize the template."""
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

    @classmethod
    def from_reaction(
        cls,
        identifier: str,
        name: str,
        reaction: Reaction,
        **kwargs: Any,
    ) -> "ReactionTemplate":
        """
        Construct a template from an existing reaction.
        """
        return cls(
            identifier=identifier,
            name=name,
            reaction=reaction,
            **kwargs,
        )

    def __repr__(self) -> str:
        return (
            "ReactionTemplate("
            f"identifier='{self.identifier}', "
            f"name='{self.name}', "
            f"category='{self.category}', "
            f"priority={self.priority}"
            ")"
        )

@dataclass
class ReactionTemplate:
    """
    Representation of a reusable reaction template.
    """

    reaction: Reaction
    name: str = "unnamed"
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_reaction(
        cls,
        reaction: Reaction,
        **kwargs: Any,
    ) -> ReactionTemplate:
        """
        Create a template from a reaction.
        """

        return cls(
            reaction=reaction,
            metadata=kwargs,
        )
