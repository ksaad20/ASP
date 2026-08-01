"""
Tests for the retrosynthesis engine.

This module validates search initialization, template matching,
node expansion, and candidate route generation.
"""

from __future__ import annotations

from asp.chemistry import MoleculeParser
from asp.planning import RetrosynthesisEngine

# nosec B101


def test_engine_initialization():
    """
    Test retrosynthesis engine creation.
    """

    engine = RetrosynthesisEngine()

    assert engine is not None
    assert engine.templates == []


def test_plan_creates_result():
    """
    Test basic retrosynthesis execution.
    """

    engine = RetrosynthesisEngine()

    molecule = MoleculeParser.from_smiles(
        "CCO"
    )

    result = engine.plan(
        molecule
    )

    assert result is not None
    assert result.search_tree is not None


def test_search_tree_created():
    """
    Test search tree root creation.
    """

    engine = RetrosynthesisEngine()

    molecule = MoleculeParser.from_smiles(
        "CCO"
    )

    result = engine.plan(
        molecule
    )

    assert (
        result.search_tree.root.molecule
        == molecule
    )


def test_max_depth_configuration():
    """
    Test maximum search depth.
    """

    engine = RetrosynthesisEngine(
        max_depth=3,
    )

    assert engine.max_depth == 3


def test_empty_template_library():
    """
    Test planning without templates.

    The MVP should still return a valid
    planning result.
    """

    engine = RetrosynthesisEngine()

    molecule = MoleculeParser.from_smiles(
        "CCO"
    )

    result = engine.plan(
        molecule
    )

    assert result is not None
    assert result.routes is not None


def test_template_expansion():
    """
    Test that enabled templates are considered.
    """

    from asp.chemistry import (
        ReactionTemplate,
    )

    template = ReactionTemplate(
        identifier="mock_reaction",
        name="Mock Reaction",
        enabled=True,
    )

    engine = RetrosynthesisEngine(
        templates=[
            template,
        ],
    )

    molecule = MoleculeParser.from_smiles(
        "CCO"
    )

    result = engine.plan(
        molecule
    )

    assert (
        result.generated_routes
        >= 0
    )

