"""
Route representation for ASP.

Defines a retrosynthetic route returned by the planning engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Route:
    """
    Representation of a retrosynthetic route.
    """

    target: Any
    steps: list[Any] = field(default_factory=list)
    score: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def step_count(self) -> int:
        """
        Return the number of steps.
        """

        return len(self.steps)

    @property
    def is_empty(self) -> bool:
        """
        Whether the route contains any reactions.
        """

        return self.step_count == 0

    def add_step(
        self,
        step: Any,
    ) -> None:
        """
        Append a reaction step.
        """

        self.steps.append(step)

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the route.
        """

        return {
            "target": getattr(
                self.target,
                "to_dict",
                lambda: self.target,
            )(),
            "steps": [
                getattr(
                    step,
                    "to_dict",
                    lambda: step,
                )()
                for step in self.steps
            ],
            "score": self.score,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "Route":
        """
        Construct a Route from a dictionary.
        """

        return cls(
            target=data.get("target"),
            steps=list(data.get("steps", [])),
            score=float(data.get("score", 0.0)),
            metadata=dict(data.get("metadata", {})),
        )

    def __len__(self) -> int:
        """
        Return the number of steps.
        """

        return self.step_count

    def __iter__(self):
        """
        Iterate over route steps.
        """

        return iter(self.steps)

    def __repr__(self) -> str:
        """
        Return a concise representation.
        """

        return (
            "Route("
            f"steps={self.step_count}, "
            f"score={self.score:.3f})"
        )
