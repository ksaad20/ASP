```python
"""
Logging utilities for Autonomous Synthesis Planner.

This module provides centralized logging configuration used across
the ASP codebase.

A unified logging system improves debugging, reproducibility, and
traceability for scientific workflows.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

from asp.constants import DEFAULT_LOG_LEVEL, LOG_FORMAT


def configure_logging(
    level: str = DEFAULT_LOG_LEVEL,
    *,
    log_file: Path | None = None,
) -> None:
    """
    Configure application-wide logging.

    Parameters
    ----------
    level
        Logging level.

    log_file
        Optional file destination.
    """

    handlers: list[logging.Handler] = []

    console_handler = logging.StreamHandler(
        sys.stdout
    )

    handlers.append(console_handler)

    if log_file is not None:
        log_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        handlers.append(
            logging.FileHandler(
                log_file,
                encoding="utf-8",
            )
        )

    logging.basicConfig(
        level=getattr(
            logging,
            level.upper(),
            logging.INFO,
        ),
        format=LOG_FORMAT,
        handlers=handlers,
        force=True,
    )


def get_logger(
    name: str,
) -> logging.Logger:
    """
    Retrieve a module logger.

    Parameters
    ----------
    name
        Logger name, usually ``__name__``.

    Returns
    -------
    logging.Logger
    """

    return logging.getLogger(name)


def set_level(
    level: str,
) -> None:
    """
    Update the root logging level.
    """

    logging.getLogger().setLevel(
        getattr(
            logging,
            level.upper(),
            logging.INFO,
        )
    )


def silence_external_loggers() -> None:
    """
    Reduce noise from third-party libraries.

    Useful for scientific workflows where external
    dependencies may generate excessive logs.
    """

    for logger_name in (
        "rdkit",
        "urllib3",
        "matplotlib",
    ):
        logging.getLogger(
            logger_name
        ).setLevel(
            logging.WARNING
        )


__all__ = [
    "configure_logging",
    "get_logger",
    "set_level",
    "silence_external_loggers",
]
```

