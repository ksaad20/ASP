```python
"""
Core molecular representation for Autonomous Synthesis Planner.

This module defines the Molecule class, the primary domain object used
throughout the planning engine.

The Molecule class acts as a lightweight wrapper around a chemical
representation (SMILES in the MVP) while remaining extensible for future
support of additional molecular formats and cheminformatics backends.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

try:
    from rdkit import Chem

    _RDKIT_AVAILABLE = True
except ImportError:  # pragma: no cover
    Chem = None
    _RDKIT_AVAILABLE = False


@dataclass(slots=True)
class Molecule:
    """
    Represents a single chemical molecule.

    Parameters
    ----------
    smiles
        Canonical or valid SMILES representation.

    name
        Optional human-readable identifier.

    metadata
        Arbitrary user-defined metadata.
    """

    smiles: str
    name: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the supplied SMILES string."""
        if not self.smiles:
            raise ValueError("SMILES string cannot be empty.")

        if _RDKIT_AVAILABLE:
            mol = Chem.MolFromSmiles(self.smiles)
            if mol is None:
                raise ValueError(
                    f"Invalid SMILES string: {self.smiles}"
                )

    @property
    def rdkit(self):
        """
        Return the underlying RDKit molecule.

        Raises
        ------
        RuntimeError
            If RDKit is unavailable.
        """
        if not _RDKIT_AVAILABLE:
            raise RuntimeError(
                "RDKit is required for molecular operations."
            )

        return Chem.MolFromSmiles(self.smiles)

    @property
    def canonical_smiles(self) -> str:
        """
        Return the canonical SMILES representation.
        """
        if not _RDKIT_AVAILABLE:
            return self.smiles

        return Chem.MolToSmiles(
            self.rdkit,
            canonical=True,
        )

    @property
    def formula(self) -> str:
        """
        Return the molecular formula.

        Returns
        -------
        str
        """
        if not _RDKIT_AVAILABLE:
            return "Unknown"

        from rdkit.Chem import rdMolDescriptors

        return rdMolDescriptors.CalcMolFormula(
            self.rdkit
        )

    @property
    def molecular_weight(self) -> float:
        """
        Return the exact molecular weight.
        """
        if not _RDKIT_AVAILABLE:
            return 0.0

        from rdkit.Chem import Descriptors

        return Descriptors.ExactMolWt(
            self.rdkit
        )

    @property
    def atom_count(self) -> int:
        """
        Number of atoms.
        """
        return self.rdkit.GetNumAtoms()

    @property
    def bond_count(self) -> int:
        """
        Number of bonds.
        """
        return self.rdkit.GetNumBonds()

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the molecule.
        """
        return {
            "name": self.name,
            "smiles": self.canonical_smiles,
            "formula": self.formula,
            "molecular_weight": self.molecular_weight,
            "atom_count": self.atom_count,
            "bond_count": self.bond_count,
            "metadata": self.metadata,
        }

    @classmethod
    def from_smiles(
        cls,
        smiles: str,
        *,
        name: str | None = None,
    ) -> "Molecule":
        """
        Construct a molecule from a SMILES string.
        """
        return cls(
            smiles=smiles,
            name=name,
        )

    def __str__(self) -> str:
        return self.canonical_smiles

    def __repr__(self) -> str:
        return (
            f"Molecule("
            f"smiles='{self.canonical_smiles}', "
            f"name={self.name!r})"
        )
```

