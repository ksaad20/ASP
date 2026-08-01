"""
Tests for molecular parsing functionality.

This module validates SMILES parsing, molecule creation,
and parser error handling.
"""

from __future__ import annotations

import pytest

from asp.chemistry import (
    MoleculeParser,
)


def test_parse_valid_smiles():
    """
    Test parsing a valid SMILES string.
    """

    molecule = MoleculeParser.from_smiles(
        "CCO"
    )

    assert molecule is not None

    assert molecule.smiles == "CCO"


def test_parse_named_molecule():
    """
    Test assigning molecule metadata.
    """

    molecule = MoleculeParser.from_smiles(
        "CCO",
        name="ethanol",
    )

    assert molecule.name == "ethanol"


def test_parse_invalid_smiles():
    """
    Test invalid SMILES handling.
    """

    with pytest.raises(
        ValueError
    ):
        MoleculeParser.from_smiles(
            "invalid_smiles"
        )


def test_empty_smiles():
    """
    Test empty input rejection.
    """

    with pytest.raises(
        ValueError
    ):
        MoleculeParser.from_smiles(
            ""
        )


def test_molecule_serialization():
    """
    Test molecule dictionary conversion.
    """

    molecule = MoleculeParser.from_smiles(
        "CCO"
    )

    data = molecule.to_dict()

    assert isinstance(
        data,
        dict,
    )

    assert (
        data["smiles"]
        == "CCO"
    )


def test_multiple_molecule_parsing():
    """
    Test parsing multiple molecules.
    """

    smiles = [
        "CCO",
        "CC",
        "O",
    ]

    molecules = [
        MoleculeParser.from_smiles(
            item
        )
        for item in smiles
    ]

    assert len(molecules) == 3

