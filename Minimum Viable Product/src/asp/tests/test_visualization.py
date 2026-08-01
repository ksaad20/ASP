"""
Tests for ASP route visualization.

This module validates graph construction, visualization object
initialization, and graph export functionality.
"""

from __future__ import annotations

import pytest

from asp.planning import Route
from asp.visualization import RouteVisualizer


class MockMolecule:
    """
    Minimal molecule object for visualization tests.
    """

    def __init__(
        self,
        identifier: str,
        name: str,
    ) -> None:
        self.identifier = identifier
        self.name = name


class MockReaction:
    """
    Minimal reaction object for visualization tests.
    """

    def __init__(self) -> None:
        self.name = "Mock Reaction"

        self.reactants = [
            MockMolecule(
                "mol_a",
                "Reactant A",
            )
        ]

        self.products = [
            MockMolecule(
                "mol_b",
                "Product B",
            )
        ]


def create_route() -> Route:
    """
    Create a minimal route.
    """

    route = Route(
        target=MockMolecule(
            "target",
            "Target",
        )
    )

    route.add_reaction(
        MockReaction()
    )

    return route


def test_visualizer_initialization():
    """
    Test visualizer creation.
    """

    visualizer = RouteVisualizer()

    assert visualizer is not None

    assert visualizer.graph is None


def test_build_graph():
    """
    Test route graph generation.
    """

    pytest.importorskip(
        "networkx"
    )

    visualizer = RouteVisualizer()

    graph = visualizer.build_graph(
        create_route()
    )

    assert graph is not None

    assert (
        len(graph.nodes)
        > 0
    )


def test_graph_contains_reaction_node():
    """
    Test reaction nodes are included.
    """

    pytest.importorskip(
        "networkx"
    )

    visualizer = RouteVisualizer()

    graph = visualizer.build_graph(
        create_route()
    )

    assert (
        "reaction_0"
        in graph.nodes
    )


def test_export_graph(
    tmp_path,
):
    """
    Test GraphML export.
    """

    pytest.importorskip(
        "networkx"
    )

    visualizer = RouteVisualizer()

    output = (
        tmp_path
        / "route.graphml"
    )

    visualizer.export_graph(
        create_route(),
        output,
    )

    assert output.exists()


def test_visualizer_graph_property():
    """
    Test current graph retrieval.
    """

    pytest.importorskip(
        "networkx"
    )

    visualizer = RouteVisualizer()

    visualizer.build_graph(
        create_route()
    )

    assert visualizer.graph is not None

