"""
Data management package for Autonomous Synthesis Planner.

This package provides data loading, storage, indexing, and repository
management for reaction templates, reaction datasets, molecular
databases, and future machine learning models.

Modules
-------
loader
    Dataset loading and parsing.

repository
    In-memory repository for reactions and templates.
"""

from .loader import DataLoader
from .repository import TemplateRepository

__all__ = [
    "DataLoader",
    "TemplateRepository",
]
