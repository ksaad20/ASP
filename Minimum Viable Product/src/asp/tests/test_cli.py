```python
"""
Tests for the ASP command-line interface.

This module verifies CLI commands, argument handling,
and output generation using Typer's testing utilities.
"""

from __future__ import annotations

from typer.testing import CliRunner

from asp.cli import app


runner = CliRunner()


def test_cli_version():
    """
    Test version command.
    """

    result = runner.invoke(
        app,
        ["version"],
    )

    assert result.exit_code == 0

    assert "ASP version" in result.output


def test_cli_info():
    """
    Test information command.
    """

    result = runner.invoke(
        app,
        ["info"],
    )

    assert result.exit_code == 0

    assert (
        "Autonomous Synthesis Planner"
        in result.output
    )


def test_cli_plan_command():
    """
    Test molecule planning command.
    """

    result = runner.invoke(
        app,
        [
            "plan",
            "molecule",
            "CCO",
        ],
    )

    assert result.exit_code == 0

    assert (
        "Generated"
        in result.output
    )


def test_cli_plan_export(
    tmp_path,
):
    """
    Test planning output export.
    """

    output = tmp_path / "route.json"

    result = runner.invoke(
        app,
        [
            "plan",
            "molecule",
            "CCO",
            "--output",
            str(output),
        ],
    )

    assert result.exit_code == 0

    assert output.exists()


def test_cli_template_load(
    tmp_path,
):
    """
    Test template loading command.
    """

    template_file = tmp_path / "templates.json"

    template_file.write_text(
        "[]",
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        [
            "templates",
            "load",
            str(template_file),
        ],
    )

    assert result.exit_code == 0

    assert (
        "Loaded"
        in result.output
    )


def test_cli_invalid_command():
    """
    Test invalid CLI input.
    """

    result = runner.invoke(
        app,
        [
            "unknown",
        ],
    )

    assert result.exit_code != 0
```

