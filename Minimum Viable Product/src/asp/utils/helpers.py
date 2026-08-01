"""
General helper utilities for Autonomous Synthesis Planner.

This module contains small, reusable functions that are shared across
different components of ASP.

Utilities here should remain lightweight and independent of domain
logic to prevent unnecessary coupling.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import TypeVar


T = TypeVar("T")


def flatten(
    items: Iterable[Iterable[T]],
) -> list[T]:
    """
    Flatten a nested iterable.

    Parameters
    ----------
    items
        Nested collection.

    Returns
    -------
    list
        Flattened list.

    Example
    -------
    >>> flatten([[1, 2], [3, 4]])
    [1, 2, 3, 4]
    """

    return [
        element
        for group in items
        for element in group
    ]


def chunked(
    items: list[T],
    size: int,
) -> Iterator[list[T]]:
    """
    Split a list into chunks.

    Parameters
    ----------
    items
        Input list.

    size
        Chunk size.

    Yields
    ------
    list
        Consecutive chunks.
    """

    if size <= 0:
        raise ValueError(
            "Chunk size must be positive."
        )

    for index in range(
        0,
        len(items),
        size,
    ):
        yield items[
            index:index + size
        ]


def unique(
    items: Iterable[T],
) -> list[T]:
    """
    Remove duplicates while preserving order.

    Parameters
    ----------
    items
        Input iterable.

    Returns
    -------
    list
        Unique values.
    """

    seen: set[T] = set()
    result: list[T] = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


def clamp(
    value: float,
    minimum: float,
    maximum: float,
) -> float:
    """
    Restrict a value to a range.
    """

    if minimum > maximum:
        raise ValueError(
            "Minimum cannot exceed maximum."
        )

    return max(
        minimum,
        min(value, maximum),
    )


def normalize(
    value: float,
    minimum: float,
    maximum: float,
) -> float:
    """
    Normalize a value to the range [0, 1].
    """

    if maximum == minimum:
        return 0.0

    return (
        (value - minimum)
        / (maximum - minimum)
    )


def safe_filename(
    filename: str,
) -> str:
    """
    Convert a string into a filesystem-safe filename.
    """

    allowed = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "-_."
    )

    return "".join(
        char
        if char in allowed
        else "_"
        for char in filename
    )


__all__ = [
    "flatten",
    "chunked",
    "unique",
    "clamp",
    "normalize",
    "safe_filename",
]

