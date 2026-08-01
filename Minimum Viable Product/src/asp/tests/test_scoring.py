"""
Tests for route scoring functionality.

This module validates route scoring, ranking,
confidence calculation, and scorer behavior.
"""

from __future__ import annotations

from asp.planning import (
    Route,
    RouteScorer,
)


class MockReaction:
    """
    Minimal reaction object for scoring tests.
    """

    def __init__(
        self,
        confidence: float,
    ) -> None:

        self.confidence = confidence

    def to_dict(self):
        return {
            "confidence": self.confidence
        }


def create_route(
    confidence: float = 0.8,
    steps: int = 2,
) -> Route:
    """
    Create a test route.
    """

    route = Route(
        target=None,
    )

    for _ in range(steps):
        route.add_reaction(
            MockReaction(
                confidence
            )
        )

    return route


def test_scorer_initialization():
    """
    Test scorer creation.
    """

    scorer = RouteScorer()

    assert scorer is not None


def test_route_step_count():
    """
    Test route step calculation.
    """

    route = create_route(
        steps=3
    )

    assert route.steps == 3


def test_average_confidence():
    """
    Test confidence averaging.
    """

    route = create_route(
        confidence=0.75,
        steps=2,
    )

    assert (
        route.average_confidence
        == 0.75
    )


def test_score_assignment():
    """
    Test score calculation.
    """

    scorer = RouteScorer()

    route = create_route()

    score = scorer.score(
        route
    )

    assert isinstance(
        score,
        float,
    )

    assert route.score == score


def test_route_ranking():
    """
    Test route ordering.
    """

    scorer = RouteScorer()

    low = create_route(
        confidence=0.2
    )

    high = create_route(
        confidence=0.9
    )

    ranked = scorer.rank(
        [
            low,
            high,
        ]
    )

    assert ranked[0] == high


def test_best_route():
    """
    Test best route selection.
    """

    scorer = RouteScorer()

    routes = [
        create_route(
            confidence=0.4
        ),
        create_route(
            confidence=0.9
        ),
    ]

    best = scorer.best(
        routes
    )

    assert best is not None


def test_empty_routes():
    """
    Test scorer with no routes.
    """

    scorer = RouteScorer()

    assert scorer.best([]) is None

