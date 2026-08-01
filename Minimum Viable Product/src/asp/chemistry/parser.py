"""
Molecule parsing utilities for ASP.

Provides validation and parsing of SMILES strings with optional
RDKit support. When RDKit is unavailable, only basic validation
is performed.
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
class ParsedMolecule:
    """
    Parsed molecular representation.
    """

    smiles: str
    valid: bool
    name: str | None = None

    def to_dict(self) -> dict[str, str | bool | None]:
        """
        Serialize the molecule.
        """

        return {
            "smiles": self.smiles,
            "valid": self.valid,
            "name": self.name,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, str | bool | None],
    ) -> "ParsedMolecule":
        """
        Construct a ParsedMolecule from a dictionary.
        """

        return cls(
            smiles=str(data["smiles"]),
            valid=bool(data["valid"]),
            name=data.get("name"),
        )


class MoleculeParser:
    """
    Parser for molecular representations.
    """

    @staticmethod
    def validate(smiles: str) -> bool:
        """
        Validate a SMILES string.

        Raises
        ------
        ValueError
            If the input is invalid.
        """

        if not isinstance(smiles, str):
            raise ValueError("SMILES must be a string.")

        smiles = smiles.strip()

        if not smiles:
            raise ValueError("SMILES cannot be empty.")

        if not _RDKIT_AVAILABLE:
            return True

        return Chem.MolFromSmiles(smiles) is not None

    @classmethod
    def from_smiles(
        cls,
        smiles: str,
        *,
        name: str | None = None,
    ) -> ParsedMolecule:
        """
        Construct a ParsedMolecule from a SMILES string.
        """

        return cls().parse(
            smiles,
            name=name,
        )

    def parse(
        self,
        smiles: str,
        *,
        name: str | None = None,
    ) -> ParsedMolecule:
        """
        Parse a SMILES string.

        Raises
        ------
        ValueError
            If the SMILES string is invalid.
        """

        if not self.validate(smiles):
            raise ValueError("Invalid SMILES.")

        return ParsedMolecule(
            smiles=smiles.strip(),
            valid=True,
            name=name,
        )


def validate_smiles(smiles: str) -> bool:
    """
    Validate a SMILES string.
    """

    return MoleculeParser.validate(smiles)


def parse_smiles(
    smiles: str,
    *,
    name: str | None = None,
) -> ParsedMolecule:
    """
    Parse a SMILES string.
    """

    return MoleculeParser.from_smiles(
        smiles,
        name=name,
    )
