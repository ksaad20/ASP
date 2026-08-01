"""
Data import utilities for Autonomous Synthesis Planner.

This module provides high-level import functions for molecules,
reactions, reaction templates, and datasets. It builds upon the
data layer while exposing a consistent API for applications,
the CLI, and notebooks.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from asp.chemistry import (
    Molecule,
    MoleculeParser,
    Reaction,
    ReactionTemplate,
)
from asp.data.loader import DataLoader


class DataImporter:
    """
    High-level data importer.
    """

    @staticmethod
    def molecule_from_smiles(
        smiles: str,
        *,
        name: str | None = None,
    ) -> Molecule:
        """
        Import a molecule from a SMILES string.
        """
        return MoleculeParser.from_smiles(
            smiles=smiles,
            name=name,
        )

    @staticmethod
    def reaction_from_smiles(
        reaction_smiles: str,
    ) -> Reaction:
        """
        Import a reaction from reaction SMILES.
        """
        return Reaction.from_smiles(
            reaction_smiles
        )

    @staticmethod
    def template_library(
        path: str | Path,
    ) -> list[ReactionTemplate]:
        """
        Import a reaction template library.
        """
        return DataLoader.load_templates(path)

    @staticmethod
    def json(
        path: str | Path,
    ) -> dict[str, Any]:
        """
        Import a JSON document.
        """
        return DataLoader.load_json(path)

    @staticmethod
    def smiles_file(
        path: str | Path,
    ) -> list[Molecule]:
        """
        Import molecules from a SMILES file.

        Each non-empty line is interpreted as
        one SMILES string.
        """

        path = Path(path)

        molecules: list[Molecule] = []

        with path.open(
            "r",
            encoding="utf-8",
        ) as handle:

            for line in handle:

                smiles = line.strip()

                if not smiles:
                    continue

                molecules.append(
                    MoleculeParser.from_smiles(
                        smiles
                    )
                )

        return molecules

    @staticmethod
    def exists(
        path: str | Path,
    ) -> bool:
        """
        Check whether a resource exists.
        """
        return DataLoader.exists(path)

    @staticmethod
    def supported_formats() -> tuple[str, ...]:
        """
        Supported import formats.
        """

        return (
            "json",
            "smiles",
            "reaction_smiles",
        )
