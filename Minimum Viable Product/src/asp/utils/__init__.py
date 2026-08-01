"""
Utility package for Autonomous Synthesis Planner.

This package contains reusable infrastructure shared across the project,
including logging, validation, and helper utilities.

The utilities are intentionally independent of the chemistry and planning
layers to avoid circular dependencies and maximize reusability.

Modules
-------
logging
    Logging configuration and utilities.

validation
    Validation helpers.

helpers
    General-purpose utility functions.
"""

from .helpers import (
    chunked,
    flatten,
    unique,
)
from .logging import get_logger
from .validation import (
    validate_identifier,
    validate_positive_integer,
)

__all__ = [
    # Logging
    "get_logger",

    # Validation
    "validate_identifier",
    "validate_positive_integer",

    # Helpers
    "flatten",
    "chunked",
    "unique",
]

