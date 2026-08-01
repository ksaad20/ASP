```python
"""
Visualization package for Autonomous Synthesis Planner.

This package provides tools for rendering and exporting synthesis
routes, reaction pathways, and planning results.

The visualization layer is separated from the planning engine so that
scientific users can generate visual outputs without affecting the
core planning workflow.

Modules
-------
routes
    Synthesis route visualization utilities.
"""

from .routes import RouteVisualizer

__all__ = [
    "RouteVisualizer",
]
```

