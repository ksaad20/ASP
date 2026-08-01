"""
Ibuprofen synthesis planning example.

This example demonstrates retrosynthetic planning for ibuprofen using
the Autonomous Synthesis Planner (ASP).

Run:

    python examples/ibuprofen.py
"""

from pathlib import Path

from asp import ASP


# Ibuprofen (2-(4-isobutylphenyl)propanoic acid) SMILES
IBUPROFEN_SMILES = (
    "CC(C)Cc1ccc(cc1)[C@H](C)C(=O)O"
)


def main() -> None:
    """
    Run ibuprofen retrosynthesis example.
    """

    print(
        "Autonomous Synthesis Planner"
    )

    print(
        "Target: Ibuprofen"
    )

    print(
        f"SMILES: {IBUPROFEN_SMILES}"
    )

    print(
        "-" * 40
    )

    planner = ASP(
        max_depth=6,
        max_routes=10,
    )

    template_path = Path(
        "datasets/templates"
    )

    if template_path.exists():

        planner.load_templates(
            template_path
        )

        print(
            "Templates loaded:",
            planner.template_count,
        )

    else:

        print(
            "Template database not found."
        )

        print(
            "Using default planner configuration."
        )

    print(
        "-" * 40
    )

    result = planner.plan(
        IBUPROFEN_SMILES
    )

    print(
        "Routes generated:",
        len(result.routes),
    )

    if result.best_route:

        print()
        print(
            "Best route score:",
            result.best_route.score,
        )

        print(
            "Synthesis steps:",
            result.best_route.steps,
        )

    else:

        print(
            "No complete synthesis route found."
        )

    output = Path(
        "ibuprofen_plan.json"
    )

    planner.export(
        result,
        output,
    )

    print()
    print(
        "Result saved:",
        output,
    )


if __name__ == "__main__":
    main()
