"""
Tests for the ASP planning interface.
"""

from __future__ import annotations

from asp.chemistry import MoleculeParser, Reaction, ReactionTemplate
from asp.planning import Planner, PlanningResult

# nosec B101


def test_planner_initialization() -> None:
    """
    Test planner construction.
    """

    planner = Planner()

    assert planner is not None
    assert len(planner) == 0


def test_planner_returns_result() -> None:
    """
    Test planning execution.
    """

    planner = Planner()

    result = planner.plan("CCO")

    assert isinstance(result, PlanningResult)


def test_planner_accepts_molecule_object() -> None:
    """
    Test planning with a molecule object.
    """

    molecule = MoleculeParser.from_smiles("CCO")

    planner = Planner()

    result = planner.plan(molecule)

    assert isinstance(result, PlanningResult)


def test_planner_max_routes() -> None:
    """
    Test route limit configuration.
    """

    planner = Planner(max_routes=5)

    assert planner.max_routes == 5


def test_planner_add_template() -> None:
    """
    Test template registration.
    """

    planner = Planner()

    reaction = Reaction.from_smiles("CCO>>CC=O")

    template = ReactionTemplate.from_reaction(
        reaction,
        identifier="test_template",
    )

    planner.add_template(template)

    assert len(planner) == 1


def test_planner_clear_templates() -> None:
    """
    Test removing all templates.
    """

    planner = Planner()

    planner.clear_templates()

    assert len(planner) == 0


def test_planner_repr() -> None:
    """
    Test planner representation.
    """

    planner = Planner()

    text = repr(planner)

    assert "Planner" in text
