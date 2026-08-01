```python
"""
Validation utilities for Autonomous Synthesis Planner.

This module provides reusable validation functions for user inputs,
configuration parameters, and domain-level constraints.

Keeping validation logic centralized prevents duplicated checks across
the chemistry, planning, CLI, and API layers.
"""

from __future__ import annotations

import re

_IDENTIFIER_PATTERN = re.compile(
    r"^[a-zA-Z0-9_\-]+$"
)


def validate_identifier(
    identifier: str,
) -> bool:
    """
    Validate a resource identifier.

    Identifiers may contain:

    - Letters
    - Numbers
    - Underscores
    - Hyphens

    Parameters
    ----------
    identifier
        Identifier to validate.

    Returns
    -------
    bool
        True if valid.
    """

    if not identifier:
        return False

    return bool(
        _IDENTIFIER_PATTERN.match(
            identifier
        )
    )


def validate_positive_integer(
    value: int,
) -> bool:
    """
    Validate a positive integer.

    Parameters
    ----------
    value
        Integer value.

    Returns
    -------
    bool
        True if greater than zero.
    """

    return (
        isinstance(value, int)
        and value > 0
    )


def validate_non_negative_float(
    value: float,
) -> bool:
    """
    Validate a non-negative floating point value.
    """

    return (
        isinstance(value, float)
        and value >= 0.0
    )


def validate_probability(
    value: float,
) -> bool:
    """
    Validate a probability value.

    Valid range:

    0.0 <= value <= 1.0
    """

    return (
        isinstance(value, float)
        and 0.0 <= value <= 1.0
    )


def validate_smiles(
    smiles: str,
) -> bool:
    """
    Validate a SMILES string.

    Uses RDKit when available. If RDKit is unavailable,
    performs basic validation only.
    """

    if not isinstance(smiles, str):
        return False

    if not smiles.strip():
        return False

    try:
        from rdkit import Chem

        molecule = Chem.MolFromSmiles(
            smiles
        )

        return molecule is not None

    except ImportError:
        return True


def require_valid_identifier(
    identifier: str,
) -> None:
    """
    Raise an exception for invalid identifiers.
    """

    if not validate_identifier(identifier):
        raise ValueError(
            f"Invalid identifier: {identifier}"
        )


def require_positive_integer(
    value: int,
    name: str = "value",
) -> None:
    """
    Raise an exception for invalid integers.
    """

    if not validate_positive_integer(value):
        raise ValueError(
            f"{name} must be a positive integer."
        )


__all__ = [
    "validate_identifier",
    "validate_positive_integer",
    "validate_non_negative_float",
    "validate_probability",
    "validate_smiles",
    "require_valid_identifier",
    "require_positive_integer",
]
```

