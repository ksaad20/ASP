```python id="7mq8rx"
"""
Synthesis route visualization for Autonomous Synthesis Planner.

This module provides visualization utilities for displaying and
exporting retrosynthetic routes.

The MVP supports graph-based visualization through NetworkX and
Matplotlib when available. The design allows future support for
interactive visualization using tools such as Plotly, Cytoscape,
and web-based interfaces.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from asp.planning.route import Route


class RouteVisualizer:
    """
    Visualizer for synthesis routes.
    """

    def __init__(
        self,
    ) -> None:

        self._graph = None

    def build_graph(
        self,
        route: Route,
    ) -> Any:
        """
        Convert a synthesis route into a graph.

        Nodes represent molecules.
        Edges represent reactions.

        Returns
        -------
        graph
            NetworkX graph object.
        """

        try:
            import networkx as nx

        except ImportError as exc:
            raise ImportError(
                "NetworkX is required for route "
                "visualization."
            ) from exc

        graph = nx.DiGraph()

        for index, reaction in enumerate(
            route.reactions
        ):

            reaction_id = (
                f"reaction_{index}"
            )

            graph.add_node(
                reaction_id,
                type="reaction",
                label=reaction.name,
            )

            for molecule in reaction.reactants:

                graph.add_node(
                    molecule.identifier,
                    type="molecule",
                    label=molecule.name,
                )

                graph.add_edge(
                    molecule.identifier,
                    reaction_id,
                )

            for molecule in reaction.products:

                graph.add_node(
                    molecule.identifier,
                    type="molecule",
                    label=molecule.name,
                )

                graph.add_edge(
                    reaction_id,
                    molecule.identifier,
                )

        self._graph = graph

        return graph

    def draw(
        self,
        route: Route,
        output: str | Path | None = None,
    ) -> Any:
        """
        Render a synthesis route.

        Parameters
        ----------
        route
            Route to visualize.

        output
            Optional output image path.
        """

        graph = self.build_graph(
            route
        )

        try:
            import matplotlib.pyplot as plt

        except ImportError as exc:
            raise ImportError(
                "Matplotlib is required for "
                "drawing routes."
            ) from exc

        position = self._layout(
            graph
        )

        plt.figure(
            figsize=(12, 8)
        )

        nx = self._networkx()

        nx.draw(
            graph,
            position,
            with_labels=True,
            node_size=1500,
        )

        if output:

            output = Path(output)

            output.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            plt.savefig(
                output,
                bbox_inches="tight",
            )

        return plt.gcf()

    def export_graph(
        self,
        route: Route,
        path: str | Path,
    ) -> None:
        """
        Export route graph as GraphML.
        """

        graph = self.build_graph(
            route
        )

        import networkx as nx

        nx.write_graphml(
            graph,
            path,
        )

    def _layout(
        self,
        graph: Any,
    ) -> dict:
        """
        Generate graph layout.
        """

        nx = self._networkx()

        return nx.spring_layout(
            graph
        )

    @staticmethod
    def _networkx():
        """
        Load NetworkX lazily.
        """

        import networkx as nx

        return nx

    @property
    def graph(self) -> Any:
        """
        Return current visualization graph.
        """

        return self._graph
```
  
