"""
Tests for the ASP public API.

This module verifies that the high-level API correctly initializes,
loads templates, executes planning, and exports results.
"""

from __future__ import annotations

import json

import pytest

from asp.api import ASP, plan


def test_api_initialization():
    """
    Test ASP application initialization.
    """

    app = ASP()

    assert app is not None
    assert app.template_count == 0


def test_plan_function_returns_result():
    """
    Test convenience planning function.
    """

    result = plan(
        "CCO"
    )

    assert result is not None
    assert hasattr(
        result,
        "routes",
    )


def test_asp_plan():
    """
    Test planning through ASP instance.
    """

    app = ASP()

    result = app.plan(
        "CCO"
    )

    assert result is not None
    assert result.target is not None


def test_export_result(
    tmp_path,
):
    """
    Test exporting planning results.
    """

    app = ASP()

    result = app.plan(
        "CCO"
    )

    output = tmp_path / "result.json"

    app.export(
        result,
        output,
    )

    assert output.exists()

    with output.open(
        "r",
        encoding="utf-8",
    ) as file:

        data = json.load(file)

    assert isinstance(
        data,
        dict,
    )


def test_template_count_property():
    """
    Test template repository integration.
    """

    app = ASP()

    assert isinstance(
        app.template_count,
        int,
    )

