"""
Data loading utilities for Autonomous Synthesis Planner.

This module provides facilities for loading reaction templates,
datasets, and other resources from disk.

The MVP supports JSON-based template libraries while providing
extension points for additional formats.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from asp.chemistry import Reaction, ReactionTemplate


class DataLoader:
    """
    Load datasets and reaction template libraries.
    """

    @staticmethod
    def load_json(
        path: str | Path,
    ) -> dict[str, Any]:
        """
        Load a JSON document.
        """

        path = Path(path)

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    @staticmethod
    def save_json(
        data: dict[str, Any],
        path: str | Path,
    ) -> None:
        """
        Save a JSON document.
        """

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                sort_keys=True,
            )

    @classmethod
    def load_templates(
        cls,
        path: str | Path,
    ) -> list[ReactionTemplate]:
        """
        Load reaction templates from a JSON file.

        Expected schema
        ---------------
        [
            {
                "identifier": "...",
                "name": "...",
                "reaction_smiles": "...",
                "category": "...",
                "priority": 100
            }
        ]
        """

        records = cls.load_json(path)

        templates: list[ReactionTemplate] = []

        for record in records:

            reaction = Reaction.from_smiles(
                record["reaction_smiles"]
            )

            template = ReactionTemplate(
                identifier=record["identifier"],
                name=record["name"],
                reaction=reaction,
                category=record.get(
                    "category",
                    "general",
                ),
                description=record.get(
                    "description",
                    "",
                ),
                priority=record.get(
                    "priority",
                    100,
                ),
                enabled=record.get(
                    "enabled",
                    True,
                ),
                metadata=record.get(
                    "metadata",
                    {},
                ),
            )

            templates.append(template)

        return templates

    @classmethod
    def save_templates(
        cls,
        templates: list[ReactionTemplate],
        path: str | Path,
    ) -> None:
        """
        Save reaction templates.
        """

        cls.save_json(
            [
                template.to_dict()
                for template in templates
            ],
            path,
        )

    @staticmethod
    def exists(
        path: str | Path,
    ) -> bool:
        """
        Check whether a resource exists.
        """

        return Path(path).exists()

    @staticmethod
    def list_files(
        directory: str | Path,
        *,
        suffix: str | None = None,
    ) -> list[Path]:
        """
        List files in a directory.
        """

        directory = Path(directory)

        if not directory.exists():
            return []

        files = sorted(
            file
            for file in directory.iterdir()
            if file.is_file()
        )

        if suffix is not None:
            files = [
                file
                for file in files
                if file.suffix == suffix
            ]

        return files
