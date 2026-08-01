"""
Chemistry module for Autonomous Synthesis Planner.

This package provides the core chemical abstractions used throughout the
planning engine, including molecular representations, reaction models,
parsers, and reaction templates.

Modules
-------
molecule
    Molecular data structures.

parser
    Molecular parsing and validation.

reaction
    Chemical reaction representations.

templates
    Reaction template management.
"""

from .molecule import Molecule
from .parser import MoleculeParser
from .reaction import Reaction
from .templates import ReactionTemplate

__all__ = [
    "Molecule",
    "MoleculeParser",
    "Reaction",
    "ReactionTemplate",
]

