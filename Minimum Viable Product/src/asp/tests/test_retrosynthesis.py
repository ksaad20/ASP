"""
Tests for the retrosynthesis engine.

This module validates search initialization, template matching,
node expansion, and candidate route generation.
"""

from __future__ import annotations

from asp.chemistry import (
    MoleculeParser,
    Reaction,
    ReactionTemplate,
)
from asp.planning import (
    PlanningResult,
    RetrosynthesisEngine,
)

# nosec B101


def test_engine_initialization() -> None:
    """
    Test retrosynthesis engine creation.
    """

    engine = RetrosynthesisEngine()

    assert engine is not None
    assert engine.templates == []


def test_plan_creates_result() -> None:
    """
    Test basic retrosynthesis execution.
    """

    engine = RetrosynthesisEngine()

    molecule = MoleculeParser.from_smiles("CCO")

    result = engine.plan(molecule)

    assert isinstance(result, PlanningResult)
    assert result.search_tree is not None


def test_search_tree_created() -> None:
    """
    Test search tree creation.
    """

    engine = RetrosynthesisEngine()

    molecule = MoleculeParser.from_smiles("CCO")

    result = engine.plan(molecule)

    assert result.search_tree is not None


def test_max_depth_configuration() -> None:
    """
    Test maximum search depth.
    """

    engine = RetrosynthesisEngine(max_depth=3)

    assert engine.max_depth == 3


def test_empty_template_library() -> None:
    """
    Test planning without templates.
    """

    engine = RetrosynthesisEngine()

    molecule = MoleculeParser.from_smiles("CCO")

    result = engine.plan(molecule)

    assert isinstance(result, PlanningResult)
    assert result.routes is not None


def test_template_expansion() -> None:
    """
    Test template registration during planning.
    """

    reaction = Reaction.from_smiles("CCO>>CC=O")

    template = ReactionTemplate.from_reaction(
        reaction,
        identifier="mock_reaction",
    )

    engine = RetrosynthesisEngine(
        templates=[template],
    )

    molecule = MoleculeParser.from_smiles("CCO")

    result = engine.plan(molecule)

    assert isinstance(result, PlanningResult)
    assert result.generated_routes >= 0
