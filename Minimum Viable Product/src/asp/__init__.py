"""
Autonomous Synthesis Planner (ASP)

An open-source software framework for AI-powered autonomous chemical
synthesis planning.

ASP provides modular tools for:

- Molecular parsing
- Retrosynthetic planning
- Reaction pathway generation
- Route optimization
- Scientific workflows

Example
-------
>>> from asp import Planner
>>> planner = Planner()
>>> result = planner.plan(target="CCO")
"""

from importlib.metadata import PackageNotFoundError, version

from .planning.planner import Planner

try:
    __version__ = version("autonomous-synthesis-planner")
except PackageNotFoundError:
    __version__ = "0.1.0"

__title__ = "Autonomous Synthesis Planner"
__package_name__ = "asp"

__author__ = "Your Name"
__license__ = "Apache-2.0"

__all__ = [
    "Planner",
    "__version__",
]
