```python
"""
Public API for Autonomous Synthesis Planner.

This module provides a stable high-level interface for integrating ASP
into external applications, notebooks, pipelines, and services.

Users should prefer this API over directly importing internal modules.
"""

from __future__ import annotations

from pathlib import Path

from asp.chemistry import Molecule
from asp.data import DataLoader, TemplateRepository
from asp.io import DataExporter
from asp.planning import Planner, PlanningResult


class ASP:
    """
    Main application interface for Autonomous Synthesis Planner.

    This class provides a unified entry point for:

    - Loading reaction templates
    - Managing planning configuration
    - Generating synthesis routes
    - Exporting results
    """

    def __init__(
        self,
        *,
        templates=None,
        max_depth: int = 5,
        max_routes: int = 20,
    ) -> None:

        self.repository = TemplateRepository(
            templates
        )

        self.planner = Planner(
            templates=self.repository.all(),
            max_depth=max_depth,
            max_routes=max_routes,
        )

    def load_templates(
        self,
        path: str | Path,
    ) -> None:
        """
        Load reaction templates from disk.
        """

        templates = DataLoader.load_templates(
            path
        )

        self.repository.clear()

        for template in templates:
            self.repository.add(template)

        self.planner.load_templates(
            templates
        )

    def plan(
        self,
        target: str | Molecule,
    ) -> PlanningResult:
        """
        Generate synthesis routes.

        Parameters
        ----------
        target
            SMILES string or Molecule object.
        """

        return self.planner.plan(
            target
        )

    def export(
        self,
        result: PlanningResult,
        path: str | Path,
    ) -> None:
        """
        Export planning results.
        """

        DataExporter.json(
            result,
            path,
        )

    @property
    def template_count(self) -> int:
        """
        Number of loaded reaction templates.
        """

        return len(
            self.repository
        )


def plan(
    target: str | Molecule,
    *,
    templates=None,
) -> PlanningResult:
    """
    Convenience planning function.

    Example
    -------
    >>> result = plan("CCO")
    """

    app = ASP(
        templates=templates
    )

    return app.plan(
        target
    )


__all__ = [
    "ASP",
    "plan",
]
```

