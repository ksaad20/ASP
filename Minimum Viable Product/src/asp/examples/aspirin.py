```python
"""
Aspirin synthesis planning example.

This example demonstrates the basic ASP workflow:

1. Initialize the planner
2. Load reaction templates
3. Define a target molecule
4. Generate retrosynthetic routes
5. Export the planning result

Run:

    python examples/aspirin.py
"""

from pathlib import Path

from asp import ASP


# Aspirin (acetylsalicylic acid) SMILES
ASPIRIN_SMILES = (
    "CC(=O)OC1=CC=CC=C1C(=O)O"
)


def main() -> None:
    """
    Run aspirin retrosynthesis example.
    """

    print(
        "Autonomous Synthesis Planner"
    )

    print(
        "Target: Aspirin"
    )

    print(
        f"SMILES: {ASPIRIN_SMILES}"
    )

    print(
        "-" * 40
    )

    # Initialize ASP
    planner = ASP(
        max_depth=5,
        max_routes=10,
    )

    # Load reaction templates if available
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
            "No template directory found."
        )

        print(
            "Running with default configuration."
        )

    print(
        "-" * 40
    )

    # Generate synthesis routes
    result = planner.plan(
        ASPIRIN_SMILES
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
            "Steps:",
            result.best_route.steps,
        )

    else:

        print(
            "No complete route found."
        )

    # Export result
    output = Path(
        "aspirin_plan.json"
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
```
