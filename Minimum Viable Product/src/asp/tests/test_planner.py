"""
Tests for the ASP planning interface.

This module validates the high-level Planner API, including
initialization, route generation, template management,
and planning results.
"""

from __future__ import annotations

from asp.planning import (
    Planner,
    PlanningResult,
)

# nosec B101


def test_planner_initialization():
    """
    Test planner construction.
    """

    planner = Planner()

    assert planner is not None

    assert planner.template_count == 0


def test_planner_returns_result():
    """
    Test planning execution.
    """

    planner = Planner()

    result = planner.plan(
        "CCO"
    )

    assert isinstance(
        result,
        PlanningResult,
    )


def test_planner_accepts_molecule_object():
    """
    Test planning with a Molecule object.
    """

    from asp.chemistry import (
        MoleculeParser,
    )

    molecule = MoleculeParser.from_smiles(
        "CCO"
    )

    planner = Planner()

    result = planner.plan(
        molecule
    )

    assert result is not None


def test_planner_max_routes():
    """
    Test route limit configuration.
    """

    planner = Planner(
        max_routes=5,
    )

    assert planner.max_routes == 5


def test_planner_add_template():
    """
    Test template registration.
    """

    from asp.chemistry import (
        ReactionTemplate,
    )

    planner = Planner()

    template = ReactionTemplate(
        identifier="test_template",
        name="Test Template",
        enabled=True,
    )

    planner.add_template(
        template
    )

    assert planner.template_count == 1


def test_planner_clear_templates():
    """
    Test removing all templates.
    """

    planner = Planner()

    planner.clear_templates()

    assert planner.template_count == 0


def test_planner_repr():
    """
    Test planner string representation.
    """

    planner = Planner()

    text = repr(
        planner
    )

    assert "Planner" in text

