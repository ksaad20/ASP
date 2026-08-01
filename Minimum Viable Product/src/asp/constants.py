```python
"""
Application-wide constants for Autonomous Synthesis Planner (ASP).

This module centralizes immutable values shared across the project.
"""

from __future__ import annotations

# =============================================================================
# Application Metadata
# =============================================================================

APP_NAME = "Autonomous Synthesis Planner"
PACKAGE_NAME = "asp"
SHORT_NAME = "ASP"

VERSION = "0.1.0"

# =============================================================================
# Chemistry
# =============================================================================

SUPPORTED_INPUT_FORMATS = (
    "smiles",
)

SUPPORTED_EXPORT_FORMATS = (
    "json",
    "csv",
)

SUPPORTED_IMAGE_FORMATS = (
    "png",
    "svg",
)

# =============================================================================
# Planning Defaults
# =============================================================================

DEFAULT_SEARCH_DEPTH = 5
DEFAULT_BEAM_WIDTH = 10
DEFAULT_MAX_ROUTES = 20
DEFAULT_TIMEOUT_SECONDS = 300

# =============================================================================
# Route Scoring
# =============================================================================

DEFAULT_COMPLEXITY_WEIGHT = 1.0
DEFAULT_CONFIDENCE_WEIGHT = 1.0
DEFAULT_ACCESSIBILITY_WEIGHT = 1.0
DEFAULT_COST_WEIGHT = 1.0

# =============================================================================
# Logging
# =============================================================================

DEFAULT_LOG_LEVEL = "INFO"

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)

# =============================================================================
# Directory Names
# =============================================================================

DATASET_DIRECTORY = "datasets"
MODEL_DIRECTORY = "models"
LOG_DIRECTORY = "logs"
OUTPUT_DIRECTORY = "outputs"
CACHE_DIRECTORY = ".cache"

# =============================================================================
# File Extensions
# =============================================================================

JSON_EXTENSION = ".json"
CSV_EXTENSION = ".csv"
PNG_EXTENSION = ".png"
SVG_EXTENSION = ".svg"

# =============================================================================
# Exit Codes
# =============================================================================

EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_INVALID_INPUT = 2
EXIT_TIMEOUT = 3

# =============================================================================
# Public Exports
# =============================================================================

__all__ = [
    "APP_NAME",
    "PACKAGE_NAME",
    "SHORT_NAME",
    "VERSION",
    "SUPPORTED_INPUT_FORMATS",
    "SUPPORTED_EXPORT_FORMATS",
    "SUPPORTED_IMAGE_FORMATS",
    "DEFAULT_SEARCH_DEPTH",
    "DEFAULT_BEAM_WIDTH",
    "DEFAULT_MAX_ROUTES",
    "DEFAULT_TIMEOUT_SECONDS",
    "DEFAULT_COMPLEXITY_WEIGHT",
    "DEFAULT_CONFIDENCE_WEIGHT",
    "DEFAULT_ACCESSIBILITY_WEIGHT",
    "DEFAULT_COST_WEIGHT",
    "DEFAULT_LOG_LEVEL",
    "LOG_FORMAT",
    "DATASET_DIRECTORY",
    "MODEL_DIRECTORY",
    "LOG_DIRECTORY",
    "OUTPUT_DIRECTORY",
    "CACHE_DIRECTORY",
]
```

