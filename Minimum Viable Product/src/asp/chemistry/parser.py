"""
SMILES parsing utilities for Autonomous Synthesis Planner.
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


class MoleculeParser:
    """
    Parser for molecular representations.

    Provides SMILES validation and parsing functionality.
    """

    def validate(self, smiles: str) -> bool:
        """
        Validate a SMILES string.
        """

        if not smiles or not isinstance(smiles, str):
            raise ValueError("Invalid SMILES")

        if not _RDKIT_AVAILABLE:
            return True

        return Chem.MolFromSmiles(smiles) is not None

    def parse(self, smiles: str) -> ParsedMolecule:
        """
        Parse a SMILES string.
        """

        return ParsedMolecule(
            smiles=smiles,
            valid=self.validate(smiles),
        )

    @classmethod
    def from_smiles(cls, smiles: str) -> ParsedMolecule:
        """
        Construct a molecule from a SMILES string.
        """

        return cls().parse(smiles)


def validate_smiles(smiles: str) -> bool:
    """
    Validate a SMILES string.
    """

    return MoleculeParser().validate(smiles)


def parse_smiles(smiles: str) -> ParsedMolecule:
    """
    Parse a SMILES string.
    """

    return MoleculeParser().parse(smiles)
