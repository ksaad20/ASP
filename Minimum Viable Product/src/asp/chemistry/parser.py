"""
Molecular parsing utilities.

This module provides the MoleculeParser responsible for converting
external molecular representations into Molecule objects.
"""

from __future__ import annotations

from pathlib import Path

try:
    from rdkit import Chem

    _RDKIT_AVAILABLE = True
except ImportError:  # pragma: no cover
    Chem = None
    _RDKIT_AVAILABLE = False

from .molecule import Molecule


class MoleculeParser:
    """
    Parser for molecular representations.

    The MVP currently supports SMILES. Additional formats such as
    SDF, MOL, and InChI can be added in future releases.
    """

    @staticmethod
    def from_smiles(
        smiles: str,
        *,
        name: str | None = None,
    ) -> Molecule:
        """
        Parse a SMILES string.

        Parameters
        ----------
        smiles
            SMILES representation.

        name
            Optional molecule name.

        Returns
        -------
        Molecule
        """
        return Molecule.from_smiles(
            smiles=smiles,
            name=name,
        )

    @staticmethod
    def validate_smiles(smiles: str) -> bool:
        """
        Validate a SMILES string.

        Returns
        -------
        bool
            True if valid.
        """
        if not smiles.strip():
            return False

        if not _RDKIT_AVAILABLE:
            return True

        return Chem.MolFromSmiles(smiles) is not None

    @staticmethod
    def canonicalize(smiles: str) -> str:
        """
        Return canonical SMILES.
        """
        if not _RDKIT_AVAILABLE:
            return smiles

        mol = Chem.MolFromSmiles(smiles)

        if mol is None:
            raise ValueError(
                f"Invalid SMILES: {smiles}"
            )

        return Chem.MolToSmiles(
            mol,
            canonical=True,
        )

    @staticmethod
    def from_file(
        path: str | Path,
    ) -> Molecule:
        """
        Load a molecule from a text file containing
        a single SMILES string.
        """
        path = Path(path)

        smiles = path.read_text(
            encoding="utf-8"
        ).strip()

        return Molecule.from_smiles(
            smiles=smiles,
            name=path.stem,
        )

    @staticmethod
    def parse_many(
        smiles_list: list[str],
    ) -> list[Molecule]:
        """
        Parse multiple SMILES strings.
        """
        return [
            Molecule.from_smiles(smiles)
            for smiles in smiles_list
        ]

    @staticmethod
    def is_supported(
        format_name: str,
    ) -> bool:
        """
        Check whether a molecular format is supported.
        """
        return format_name.lower() in {
            "smiles",
        }

