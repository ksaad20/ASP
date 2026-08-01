"""
Caffeine synthesis planning example.

This example demonstrates retrosynthetic planning for caffeine using
the Autonomous Synthesis Planner (ASP).

Run:

    python examples/caffeine.py
"""

from pathlib import Path

from asp import ASP


# Caffeine (1,3,7-trimethylxanthine) SMILES
CAFFEINE_SMILES = (
    "Cn1cnc2n(C)c(=O)n(C)c(=O)c12"
)


def main() -> None:
    """
    Run caffeine retrosynthesis example.
    """

    print(
        "Autonomous Synthesis Planner"
    )

    print(
        "Target: Caffeine"
    )

    print(
        f"SMILES: {CAFFEINE_SMILES}"
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
        CAFFEINE_SMILES
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
        "caffeine_plan.json"
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
