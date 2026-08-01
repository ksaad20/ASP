"""
Command-line interface for Autonomous Synthesis Planner.

This module provides terminal commands for running synthesis planning,
managing reaction templates, and exporting results.

The CLI is built using Typer to provide a modern, developer-friendly
command interface.
"""

"""
ASP command line interface.
"""

from __future__ import annotations

# ruff: noqa: B008

from pathlib import Path

import typer

from asp.api import ASP
from asp.io import DataExporter
from asp.utils.logging import configure_logging


app = typer.Typer(
    name="asp",
    help=(
        "Autonomous Synthesis Planner - "
        "AI-assisted retrosynthetic planning."
    ),
)


planner_app = typer.Typer(
    help="Synthesis planning commands."
)

template_app = typer.Typer(
    help="Reaction template management."
)


app.add_typer(
    planner_app,
    name="plan",
)

app.add_typer(
    template_app,
    name="templates",
)


asp_instance = ASP()


@planner_app.command()
def molecule(
    target: str = typer.Argument(
        ...,
        help="Target molecule SMILES string.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output JSON file.",
    ),
) -> None:
    """
    Generate synthesis routes for a molecule.
    """

    configure_logging()

    result = asp_instance.plan(
        target
    )

    typer.echo(
        f"Generated {len(result)} routes."
    )

    if result.best_route:

        typer.echo(
            "Best route score: "
            f"{result.best_route.score:.4f}"
        )

    if output:

        DataExporter.json(
            result,
            output,
        )

        typer.echo(
            f"Saved result to {output}"
        )


@template_app.command(
    "load",
)
def load_templates(
    path: Path = typer.Argument(
        ...,
        help="Template JSON file.",
    ),
) -> None:
    """
    Load reaction templates.
    """

    asp_instance.load_templates(
        path
    )

    typer.echo(
        "Loaded "
        f"{asp_instance.template_count} "
        "templates."
    )


@app.command()
def version() -> None:
    """
    Display ASP version.
    """

    from asp import __version__

    typer.echo(
        f"ASP version {__version__}"
    )


@app.command()
def info() -> None:
    """
    Display system information.
    """

    typer.echo(
        "Autonomous Synthesis Planner"
    )

    typer.echo(
        f"Templates loaded: "
        f"{asp_instance.template_count}"
    )


def main() -> None:
    """
    CLI entry point.
    """

    app()


if __name__ == "__main__":
    main()
