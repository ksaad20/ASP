"""
Planning package for Autonomous Synthesis Planner.

This package contains the core planning algorithms, orchestration layer,
optimization routines, and domain models that collectively implement
autonomous retrosynthetic planning.

Architecture
------------
Planner
    High-level public API.

PlanningEngine
    Coordinates planning, scoring, and optimization.

RetrosynthesisEngine
    Generates candidate synthesis routes.

RouteScorer
    Scores and ranks synthesis routes.

RouteOptimizer
    Optimizes and filters candidate routes.

Route
    Domain model representing a synthesis pathway.

PlanningResult
    Result object returned by the planning engine.

SearchTree
    Search tree used during route generation.
"""

from .engine import PlanningEngine
from .optimizer import RouteOptimizer
from .planner import Planner
from .result import PlanningResult, PlanningStatistics
from .retrosynthesis import RetrosynthesisEngine
from .route import Route
from .scoring import RouteScorer
from .search import SearchNode, SearchTree

__all__ = [
    # Public API
    "Planner",
    "PlanningEngine",

    # Planning algorithms
    "RetrosynthesisEngine",
    "RouteScorer",
    "RouteOptimizer",

    # Domain models
    "Route",
    "PlanningResult",
    "PlanningStatistics",

    # Search structures
    "SearchNode",
    "SearchTree",
]
