"""
Template repository for Autonomous Synthesis Planner.

The TemplateRepository provides an in-memory repository for managing
reaction templates. It acts as the central data source for the
planning engine and can later be extended with persistent storage,
database backends, and remote repositories.
"""

from __future__ import annotations

from collections.abc import Iterator

from asp.chemistry import Molecule, ReactionTemplate


class TemplateRepository:
    """
    Repository for reaction templates.
    """

    def __init__(
        self,
        templates: list[ReactionTemplate] | None = None,
    ) -> None:

        self._templates: dict[
            str,
            ReactionTemplate,
        ] = {}

        if templates:
            for template in templates:
                self.add(template)

    def add(
        self,
        template: ReactionTemplate,
    ) -> None:
        """
        Register a template.
        """

        self._templates[
            template.identifier
        ] = template

    def remove(
        self,
        identifier: str,
    ) -> bool:
        """
        Remove a template.
        """

        return (
            self._templates.pop(
                identifier,
                None,
            )
            is not None
        )

    def clear(self) -> None:
        """
        Remove every template.
        """

        self._templates.clear()

    def get(
        self,
        identifier: str,
    ) -> ReactionTemplate | None:
        """
        Retrieve a template.
        """

        return self._templates.get(
            identifier
        )

    def exists(
        self,
        identifier: str,
    ) -> bool:
        """
        Check if a template exists.
        """

        return identifier in self._templates

    def all(self) -> list[ReactionTemplate]:
        """
        Return all templates.
        """

        return list(
            self._templates.values()
        )

    def enabled(self) -> list[ReactionTemplate]:
        """
        Return enabled templates.
        """

        return [
            template
            for template in self._templates.values()
            if template.enabled
        ]

    def by_category(
        self,
        category: str,
    ) -> list[ReactionTemplate]:
        """
        Return templates belonging to a category.
        """

        return [
            template
            for template in self._templates.values()
            if template.category == category
        ]

    def applicable(
        self,
        molecule: Molecule,
    ) -> list[ReactionTemplate]:
        """
        Return templates applicable to a molecule.

        MVP implementation returns every enabled
        template.

        Future versions will perform SMARTS matching,
        graph matching, fingerprint similarity,
        or learned template retrieval.
        """

        del molecule

        return self.enabled()

    def __len__(self) -> int:
        return len(self._templates)

    def __iter__(
        self,
    ) -> Iterator[ReactionTemplate]:
        return iter(
            self._templates.values()
        )

    def __contains__(
        self,
        identifier: str,
    ) -> bool:
        return self.exists(identifier)

    def __repr__(self) -> str:
        return (
            "TemplateRepository("
            f"templates={len(self)})"
        )
