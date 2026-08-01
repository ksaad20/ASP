"""
SMILES parsing utilities.
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


class MoleculeParser:
    """
    Parser for molecular representations.
    """

    @classmethod
    def from_smiles(
        cls,
        smiles: str,
        *,
        name: str | None = None,
    ) -> ParsedMolecule:
        """
        Create a ParsedMolecule from a SMILES string.
        """

        return cls().parse(
            smiles,
            name=name,
        )

    def validate(
        self,
        smiles: str,
    ) -> bool:
        """
        Validate a SMILES string.
        """

        if not isinstance(smiles, str) or not smiles.strip():
            raise ValueError("Invalid SMILES.")

        if not _RDKIT_AVAILABLE:
            return True

        return Chem.MolFromSmiles(smiles) is not None

    def parse(
        self,
        smiles: str,
        *,
        name: str | None = None,
    ) -> ParsedMolecule:
        """
        Parse a SMILES string.
        """

        valid = self.validate(smiles)

        if not valid:
            raise ValueError("Invalid SMILES.")

        return ParsedMolecule(
            smiles=smiles,
            valid=True,
            name=name,
        )


def validate_smiles(smiles: str) -> bool:
    """
    Validate a SMILES string.
    """

    return MoleculeParser().validate(smiles)


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
