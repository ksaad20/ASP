"""
Search tree data structures for ASP.

Defines the search nodes and tree used during retrosynthetic
planning.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class SearchNode:
    """
    Node in the retrosynthetic search tree.
    """

    molecule: Any
    parent: SearchNode | None = None
    children: list[SearchNode] = field(default_factory=list)
    score: float = 0.0
    expanded: bool = False

    def add_child(self, child: SearchNode) -> None:
        """
        Add a child node.
        """

        child.parent = self
        self.children.append(child)

    @property
    def is_root(self) -> bool:
        """
        Whether this node is the root node.
        """

        return self.parent is None

    @property
    def is_leaf(self) -> bool:
        """
        Whether this node is a leaf.
        """

        return not self.children

    @property
    def path(self) -> list[SearchNode]:
        """
        Return the path from the root node to this node.
        """

        node: SearchNode | None = self
        path: list[SearchNode] = []

        while node is not None:
            path.append(node)
            node = node.parent

        path.reverse()
        return path

    def __iter__(self) -> Iterator[SearchNode]:
        """
        Iterate over immediate children.
        """

        return iter(self.children)


@dataclass(slots=True)
class SearchTree:
    """
    Search tree used by the retrosynthesis engine.
    """

    root: SearchNode | None = None

    def __post_init__(self) -> None:
        """
        Ensure a valid root exists.
        """

        if self.root is None:
            self.root = SearchNode(molecule=None)

    def __iter__(self) -> Iterator[SearchNode]:
        """
        Iterate over the tree in depth-first order.
        """

        yield from self.depth_first()

    def depth_first(self) -> Iterator[SearchNode]:
        """
        Depth-first traversal.
        """

        stack: list[SearchNode] = [self.root]

        while stack:
            node = stack.pop()
            yield node
            stack.extend(reversed(node.children))

    def breadth_first(self) -> Iterator[SearchNode]:
        """
        Breadth-first traversal.
        """

        queue: list[SearchNode] = [self.root]

        while queue:
            node = queue.pop(0)
            yield node
            queue.extend(node.children)

    @property
    def size(self) -> int:
        """
        Return the number of nodes in the tree.
        """

        return sum(1 for _ in self.depth_first())

    @property
    def leaves(self) -> list[SearchNode]:
        """
        Return all leaf nodes.
        """

        return [
            node
            for node in self.depth_first()
            if node.is_leaf
        ]

    def add_root(self, molecule: Any) -> SearchNode:
        """
        Replace the root node.
        """

        self.root = SearchNode(molecule=molecule)
        return self.root

    def clear(self) -> None:
        """
        Reset the search tree.
        """

        self.root = SearchNode(molecule=None)

    def __len__(self) -> int:
        """
        Return the number of nodes.
        """

        return self.size

    def __repr__(self) -> str:
        """
        Return a concise representation.
        """

        return f"SearchTree(nodes={self.size})"
