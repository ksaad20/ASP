"""
Molecule parsing utilities for ASP.

Provides lightweight SMILES parsing with optional RDKit
validation and a fallback implementation for environments
where RDKit is unavailable.
"""

from __future__ import annotations

from dataclasses import dataclass

try:
    from rdkit import Chem

    _RDKIT_AVAILABLE = True
except ImportError:  # pragma: no cover
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

    def to_dict(self) -> dict[str, object]:
        """
        Serialize the molecule.
        """

        return {
            "smiles": self.smiles,
            "valid": self.valid,
            "name": self.name,
        }


class MoleculeParser:
    """
    Parser for molecular representations.
    """

    @staticmethod
    def validate(
        smiles: str,
    ) -> bool:
        """
        Validate a SMILES string.

        Raises
        ------
        ValueError
            If the input is empty or not a string.
        """

        if not isinstance(smiles, str):
            raise ValueError("Invalid SMILES.")

        smiles = smiles.strip()

        if not smiles:
            raise ValueError("Invalid SMILES.")

        if _RDKIT_AVAILABLE:
            return Chem.MolFromSmiles(smiles) is not None

        #
        # Lightweight fallback validation.
        #
        allowed = set(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz"
            "0123456789"
            "()[]=#@+-/\\."
        )

        return all(char in allowed for char in smiles)

    @classmethod
    def from_smiles(
        cls,
        smiles: str,
        name: str | None = None,
    ) -> ParsedMolecule:
        """
        Construct a ParsedMolecule from a SMILES string.
        """

        parser = cls()

        valid = parser.validate(smiles)

        if not valid:
            raise ValueError("Invalid SMILES.")

        return ParsedMolecule(
            smiles=smiles,
            valid=True,
            name=name,
        )

    def parse(
        self,
        smiles: str,
        name: str | None = None,
    ) -> ParsedMolecule:
        """
        Parse a SMILES string.
        """

        return self.from_smiles(
            smiles=smiles,
            name=name,
        )


def validate_smiles(
    smiles: str,
) -> bool:
    """
    Validate a SMILES string.
    """

    return MoleculeParser.validate(smiles)


def parse_smiles(
    smiles: str,
    name: str | None = None,
) -> ParsedMolecule:
    """
    Parse a SMILES string.
    """

    return MoleculeParser.from_smiles(
        smiles=smiles,
        name=name,
    )
