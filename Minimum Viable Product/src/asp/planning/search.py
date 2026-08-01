"""
Search infrastructure for Autonomous Synthesis Planner.

This module defines the core search data structures used by the planning
engine. The MVP provides a generic search tree abstraction that can support
breadth-first search, depth-first search, beam search, and future heuristic
search algorithms.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field

from asp.chemistry import Molecule


@dataclass(slots=True)
class SearchNode:
    """
    A node in the retrosynthetic search tree.

    Parameters
    ----------
    molecule
        Target molecule represented by this node.

    depth
        Depth within the search tree.

    score
        Heuristic search score.

    parent
        Parent search node.

    children
        Expanded child nodes.
    """

    molecule: Molecule

    depth: int = 0

    score: float = 0.0

    parent: "SearchNode | None" = None

    children: list["SearchNode"] = field(default_factory=list)

    expanded: bool = False

    def add_child(
        self,
        child: "SearchNode",
    ) -> None:
        """
        Add a child node.
        """
        child.parent = self
        self.children.append(child)

    @property
    def is_leaf(self) -> bool:
        """Return True if the node has no children."""
        return len(self.children) == 0

    @property
    def path(self) -> list["SearchNode"]:
        """
        Return the path from the root node to this node.
        """
        node = self
        nodes: list[SearchNode] = []

        while node is not None:
            nodes.append(node)
            node = node.parent

        return list(reversed(nodes))


class SearchTree:
    """
    Search tree used during retrosynthetic planning.
    """

    def __init__(
        self,
        root: Molecule,
    ) -> None:
        self.root = SearchNode(root)

    def breadth_first(self):
        """
        Breadth-first traversal.
        """
        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            yield node

            queue.extend(node.children)

    def depth_first(self):
        """
        Depth-first traversal.
        """
        stack = [self.root]

        while stack:
            node = stack.pop()

            yield node

            stack.extend(reversed(node.children))

    def leaves(self) -> list[SearchNode]:
        """
        Return all leaf nodes.
        """
        return [
            node
            for node in self.depth_first()
            if node.is_leaf
        ]

    def size(self) -> int:
        """
        Total number of nodes.
        """
        return sum(
            1
            for _ in self.depth_first()
        )

    def max_depth(self) -> int:
        """
        Maximum tree depth.
        """
        return max(
            node.depth
            for node in self.depth_first()
        )

    def __iter__(self):
        """
        Iterate depth-first.
        """
        return self.depth_first()
