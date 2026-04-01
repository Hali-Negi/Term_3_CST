"""
Assignment 1 - Snake Game
COMP 3522
Author: Hali Imanpanah
Student ID: A01363782
Date: Winter 2026
"""

from collections import deque
from typing import List, Tuple, Optional, Set, Dict
from pathfinding_strategy import PathfindingStrategy

GridPos = Tuple[int, int]

UP: GridPos = (0, -1)
DOWN: GridPos = (0, 1)
LEFT: GridPos = (-1, 0)
RIGHT: GridPos = (1, 0)

DIRS = [UP, DOWN, LEFT, RIGHT]


class BFSStrategy(PathfindingStrategy):
    """
    Concrete pathfinding strategy implementing the
    Breadth-First Search (BFS) algorithm.

    This class computes the shortest path between two grid positions
    while avoiding blocked cells.
    """

    def find_path(
            self,
            start: GridPos,
            goal: GridPos,
            blocked: Set[GridPos],
            cols: int,
            rows: int
    ) -> Optional[List[GridPos]]:
        """
        Find shortest path from start to goal using BFS.

        :param start: starting grid position
        :param goal: target grid position (food)
        :param blocked: set of blocked cells (snake body)
        :param cols: number of grid columns
        :param rows: number of grid rows
        :return: list of positions from start to goal, or None if no path
        """

        # BFS explores the grid level by level outward from the snake's head,
        # tracking how it arrived at each cell,
        # until it reaches the food
        # then it traces back to reconstruct the shortest path."
        if start == goal:
            return [start]

        q = deque([start])
        came_from: Dict[GridPos, GridPos] = {}
        visited: Set[GridPos] = {start}

        while q:
            cur = q.popleft()
            for dc, dr in DIRS:
                nxt = (cur[0] + dc, cur[1] + dr)

                if nxt in visited:
                    continue
                if nxt in blocked:
                    continue
                if nxt[0] < 0 or nxt[0] >= cols or nxt[1] < 0 or nxt[1] >= rows:
                    continue

                visited.add(nxt)
                came_from[nxt] = cur

                if nxt == goal:
                    # Reconstruct path from goal back to start
                    path = [goal]
                    while path[-1] != start:
                        path.append(came_from[path[-1]])
                    path.reverse()
                    return path

                q.append(nxt)

        return None


class DFSStrategy(PathfindingStrategy):
    name = "DFS"

    def find_path(self, start, goal, obstacles, cols, rows):
        stack = [start]
        parent: Dict[GridPos, Optional[GridPos]] = {start: None}

        while stack:
            cur = stack.pop()
            if cur == goal:
                return self._reconstruct(parent, goal)

            x, y = cur
            for nb in self._neighbors(x, y, cols, rows, obstacles):
                if nb not in parent:
                    parent[nb] = cur
                    stack.append(nb)

        return None
