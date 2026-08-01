"""
Molecule representation.
"""

from __future__ import annotations

from dataclasses import dataclass

try:
    from rdkit import Chem

    _RDKIT_AVAILABLE = True
except ImportError:
    Chem = None
    _RDKIT_AVAILABLE = False


@dataclass(slots=True)
class Molecule:
    """
    Representation of a molecule.
    """

    smiles: str
    name: str | None = None

    def __post_init__(self) -> None:
        """
        Validate the molecule.
        """

        if not isinstance(self.smiles, str) or not self.smiles.strip():
            raise ValueError("Invalid SMILES.")

        if _RDKIT_AVAILABLE:
            if Chem.MolFromSmiles(self.smiles) is None:
                raise ValueError("Invalid SMILES.")

    @property
    def valid(self) -> bool:
        """
        Whether the molecule is valid.
        """

        return True

    def to_dict(self) -> dict[str, str | None]:
        """
        Serialize the molecule.
        """

        return {
            "smiles": self.smiles,
            "name": self.name,
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

    def copy(self) -> "Molecule":
        """
        Return a shallow copy.
        """

        return Molecule(
            smiles=self.smiles,
            name=self.name,
        )

    def __str__(self) -> str:
        """
        Return the SMILES representation.
        """

        return self.smiles
