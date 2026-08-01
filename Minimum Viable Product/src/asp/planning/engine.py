```python
"""
Planning engine for Autonomous Synthesis Planner.

This module coordinates the complete planning pipeline, including
retrosynthetic search, route scoring, and optimization.
"""

from __future__ import annotations

import time

from asp.chemistry import Molecule, ReactionTemplate

from .optimizer import RouteOptimizer
from .result import PlanningResult
from .retrosynthesis import RetrosynthesisEngine
from .scoring import RouteScorer


class PlanningEngine:
    """
    Coordinates the complete synthesis planning workflow.
    """

    def __init__(
        self,
        *,
        templates: list[ReactionTemplate] | None = None,
        scorer: RouteScorer | None = None,
        optimizer: RouteOptimizer | None = None,
        max_depth: int = 5,
        max_routes: int = 20,
    ) -> None:
        self.retrosynthesis = RetrosynthesisEngine(
            templates=templates,
            max_depth=max_depth,
        )

        self.scorer = scorer or RouteScorer()
        self.optimizer = optimizer or RouteOptimizer()

        self.max_routes = max_routes

    def plan(
        self,
        target: Molecule,
    ) -> PlanningResult:
        """
        Execute the complete planning pipeline.
        """

        start = time.perf_counter()

        result = self.retrosynthesis.plan(target)

        result.routes = self.scorer.rank(
            result.routes
        )

        result.routes = self.optimizer.optimize(
            result.routes
        )

        result.routes = result.routes[: self.max_routes]

        result.statistics.evaluated_routes = (
            len(result.routes)
        )

        result.statistics.elapsed_time = (
            time.perf_counter() - start
        )

        return result

    @property
    def template_count(self) -> int:
        """
        Number of registered templates.
        """
        return len(self.retrosynthesis.templates)

    def add_template(
        self,
        template: ReactionTemplate,
    ) -> None:
        """
        Register a reaction template.
        """
        self.retrosynthesis.templates.append(
            template
        )

    def remove_template(
        self,
        identifier: str,
    ) -> bool:
        """
        Remove a template by identifier.
        """

        templates = self.retrosynthesis.templates

        for template in templates:
            if template.identifier == identifier:
                templates.remove(template)
                return True

        return False

    def clear_templates(self) -> None:
        """
        Remove all templates.
        """
        self.retrosynthesis.templates.clear()

    def load_templates(
        self,
        templates: list[ReactionTemplate],
    ) -> None:
        """
        Replace the current template library.
        """
        self.retrosynthesis.templates = list(
            templates
        )
```

