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

    Attributes
    ----------
    smiles:
        Original SMILES string.
    valid:
        Whether the SMILES is valid.
    """

    smiles: str
    valid: bool


def validate_smiles(smiles: str) -> bool:
    """
    Validate a SMILES string.

    Parameters
    ----------
    smiles:
        SMILES representation.

    Returns
    -------
    bool
        True if valid.

    Raises
    ------
    ValueError
        If the input is empty or not a string.
    """

    if not smiles or not isinstance(smiles, str):
        raise ValueError("Invalid SMILES")

    if not _RDKIT_AVAILABLE:
        return True

    return Chem.MolFromSmiles(smiles) is not None


def parse_smiles(smiles: str) -> ParsedMolecule:
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

    valid = validate_smiles(smiles)

    return ParsedMolecule(
        smiles=smiles,
        valid=valid,
    )


def serialize_molecule(molecule: ParsedMolecule) -> dict[str, object]:
    """
    Serialize a parsed molecule.

    Parameters
    ----------
    molecule:
        Parsed molecule.

    Returns
    -------
    dict
        Serializable representation.
    """

    return {
        "smiles": molecule.smiles,
        "valid": molecule.valid,
    }
```
