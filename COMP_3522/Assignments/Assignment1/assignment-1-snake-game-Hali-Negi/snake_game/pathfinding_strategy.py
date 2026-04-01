"""
Assignment 1 - Snake Game
COMP 3522
Author: Hali Imanpanah
Student ID: A01363782
Date: Winter 2026
"""

from abc import ABC, abstractmethod


class PathfindingStrategy(ABC):
    """
    Abstract base class for pathfinding strategies.
    """

    @abstractmethod
    def find_path(self, start, goal, blocked, cols, rows):
        """
        Return a path from start to goal while avoiding blocked cells.

        :param start: starting grid position
        :param goal: target grid position
        :param blocked: positions that cannot be used
        :param cols: number of grid columns
        :param rows: number of grid rows
        :return: a list path
        """
        raise NotImplementedError
