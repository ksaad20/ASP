from __future__ import annotations

from dataclasses import dataclass

try:
    from rdkit import Chem

    _RDKIT_AVAILABLE = True
except ImportError:
    Chem = None
    _RDKIT_AVAILABLE = False


@dataclass
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

        Parameters
        ----------
        smiles:
            SMILES representation.

        Returns
        -------
        bool
            Whether the SMILES is valid.

        Raises
        ------
        ValueError
            If SMILES input is invalid.
        """

        if not smiles or not isinstance(smiles, str):
            raise ValueError("Invalid SMILES")

        if not _RDKIT_AVAILABLE:
            return True

        return Chem.MolFromSmiles(smiles) is not None
        
    @classmethod
    def from_smiles(cls, smiles: str) -> ParsedMolecule:
    """
    Create a molecule from a SMILES string.
    """

    parser = cls()
    return parser.parse(smiles)

    def parse(self, smiles: str) -> ParsedMolecule:
        """
        Parse a SMILES string.

        Parameters
        ----------
        smiles:
            SMILES representation.

        Returns
        -------
        ParsedMolecule
            Parsed molecule object.
        """

        return ParsedMolecule(
            smiles=smiles,
            valid=self.validate(smiles),
        )


def validate_smiles(smiles: str) -> bool:
    """
    Validate a SMILES string using MoleculeParser.
    """

    return MoleculeParser().validate(smiles)


def parse_smiles(smiles: str) -> ParsedMolecule:
    """
    Parse a SMILES string using MoleculeParser.
    """

    return MoleculeParser().parse(smiles)

@classmethod
def from_smiles(cls, smiles: str):
    return cls().parse(smiles)
