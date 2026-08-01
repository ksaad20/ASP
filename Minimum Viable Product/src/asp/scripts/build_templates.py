"""
Reaction template builder for Autonomous Synthesis Planner.

This script converts reaction datasets into ASP-compatible reaction
template libraries.

The MVP implementation supports JSON-based reaction records.

Expected input format:

[
    {
        "id": "reaction_001",
        "name": "Esterification",
        "reaction_smiles": "reactants>>products",
        "category": "functional_group_transformation"
    }
]

Run:

    python scripts/build_templates.py
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_INPUT = Path(
    "datasets/reactions"
)

DEFAULT_OUTPUT = Path(
    "datasets/templates/templates.json"
)


def load_reactions(
    directory: Path,
) -> list[dict]:
    """
    Load reaction records from JSON files.
    """

    reactions = []

    if not directory.exists():

        return reactions

    for file in directory.glob(
        "*.json"
    ):

        with file.open(
            "r",
            encoding="utf-8",
        ) as handle:

            data = json.load(
                handle
            )

            if isinstance(
                data,
                list,
            ):

                reactions.extend(
                    data
                )

    return reactions


def build_template(
    reaction: dict,
) -> dict:
    """
    Convert a reaction record into
    an ASP template definition.
    """

    return {
        "identifier": reaction.get(
            "id",
            "unknown",
        ),
        "name": reaction.get(
            "name",
            "Unnamed Reaction",
        ),
        "reaction_smiles": reaction.get(
            "reaction_smiles",
            "",
        ),
        "category": reaction.get(
            "category",
            "general",
        ),
        "priority": reaction.get(
            "priority",
            100,
        ),
        "enabled": True,
        "metadata": {
            "source": "ASP template builder"
        },
    }


def build_templates(
    input_directory: Path,
    output_file: Path,
) -> None:
    """
    Build and save template library.
    """

    reactions = load_reactions(
        input_directory
    )

    templates = [
        build_template(
            reaction
        )
        for reaction in reactions
    ]

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_file.open(
        "w",
        encoding="utf-8",
    ) as handle:

        json.dump(
            templates,
            handle,
            indent=4,
        )

    print(
        f"Generated {len(templates)} templates."
    )

    print(
        f"Saved: {output_file}"
    )


def main() -> None:
    """
    Command-line entry point.
    """

    parser = argparse.ArgumentParser(
        description=(
            "Build ASP reaction templates."
        )
    )

    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help=(
            "Reaction dataset directory."
        ),
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=(
            "Template output path."
        ),
    )

    args = parser.parse_args()

    build_templates(
        args.input,
        args.output,
    )


if __name__ == "__main__":
    main()
