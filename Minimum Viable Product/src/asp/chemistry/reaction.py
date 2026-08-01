"""
Chemical reaction domain model.

This module defines the Reaction class, which represents a single
chemical transformation between reactants and products.

The Reaction object serves as the fundamental unit of retrosynthetic
planning and reaction network construction.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .molecule import Molecule


@dataclass(slots=True)
class Reaction:
    """
    Represents a chemical reaction.

    Parameters
    ----------
    reactants
        Molecules consumed by the reaction.

    products
        Molecules produced by the reaction.

    reagents
        Optional catalysts, solvents, or additives.

    conditions
        Experimental reaction conditions.

    metadata
        User-defined metadata.

    confidence
        Confidence score associated with the reaction.
    """

    reactants: list[Molecule]
    products: list[Molecule]

    reagents: list[str] = field(default_factory=list)

    conditions: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    confidence: float = 1.0

    def __post_init__(self) -> None:
        """Validate the reaction."""

        if not self.reactants:
            raise ValueError(
                "A reaction must contain at least one reactant."
            )

        if not self.products:
            raise ValueError(
                "A reaction must contain at least one product."
            )

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(
                "confidence must lie between 0 and 1."
            )

    @property
    def reactant_count(self) -> int:
        """Number of reactants."""
        return len(self.reactants)

    @property
    def product_count(self) -> int:
        """Number of products."""
        return len(self.products)

    @property
    def reaction_smiles(self) -> str:
        """
        Return a reaction SMILES representation.

        Format
        ------
        reactant1.reactant2>>product1.product2
        """

        reactants = ".".join(
            molecule.canonical_smiles
            for molecule in self.reactants
        )

        products = ".".join(
            molecule.canonical_smiles
            for molecule in self.products
        )

        return f"{reactants}>>{products}"

    @property
    def is_balanced(self) -> bool:
        """
        Placeholder for reaction balancing.

        Future versions will perform elemental
        and charge balance validation.
        """
        return True

    def contains_molecule(
        self,
        molecule: Molecule,
    ) -> bool:
        """
        Check whether a molecule participates
        in the reaction.
        """
        smiles = molecule.canonical_smiles

        return any(
            m.canonical_smiles == smiles
            for m in (
                self.reactants + self.products
            )
        )

    def to_dict(self) -> dict[str, Any]:
        """Serialize the reaction."""

        return {
            "reactants": [
                molecule.to_dict()
                for molecule in self.reactants
            ],
            "products": [
                molecule.to_dict()
                for molecule in self.products
            ],
            "reagents": self.reagents,
            "conditions": self.conditions,
            "confidence": self.confidence,
            "metadata": self.metadata,
            "reaction_smiles": self.reaction_smiles,
        }

    @classmethod
    def from_smiles(
        cls,
        reaction_smiles: str,
    ) -> "Reaction":
        """
        Construct a Reaction from reaction SMILES.

        Expected format
        ---------------
        reactants>>products

        Example
        -------
        CCO.O>>CC=O
        """

        if ">>" not in reaction_smiles:
            raise ValueError(
                "Invalid reaction SMILES."
            )

        reactant_part, product_part = (
            reaction_smiles.split(">>", maxsplit=1)
        )

        reactants = [
            Molecule.from_smiles(smiles)
            for smiles in reactant_part.split(".")
            if smiles
        ]

        products = [
            Molecule.from_smiles(smiles)
            for smiles in product_part.split(".")
            if smiles
        ]

        return cls(
            reactants=reactants,
            products=products,
        )

    def __str__(self) -> str:
        return self.reaction_smiles

    def __repr__(self) -> str:
        return (
            "Reaction("
            f"{self.reaction_smiles}, "
            f"confidence={self.confidence:.2f}"
            ")"
        )

