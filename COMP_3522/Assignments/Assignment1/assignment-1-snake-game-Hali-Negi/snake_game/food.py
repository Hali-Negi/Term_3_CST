"""
Assignment 1 - Snake Game
COMP 3522
Author: Hali Imanpanah
Student ID: A01363782
Date: Winter 2026
"""
import random
from typing import Tuple, List
from settings import GRID_COLS, GRID_ROWS

GridPos = Tuple[int, int]


class Food:
    """
    Represents a food item that appears on the game grid
    Handles random spawning and respawning outside the snake body.
    """

    def __init__(self):
        """
        Initialize the food at a random position on the grid.
        """
        self.position: GridPos = self._random_position()

    def _random_position(self) -> GridPos:
        """
        Generate a random valid grid position for the food.
        :return: A tuple (col, row) within the grid boundaries.
        """
        return (
            random.randint(0, GRID_COLS - 1),
            random.randint(0, GRID_ROWS - 1)
        )

    def respawn(self, blocked: List[GridPos]):
        """
        Respawns the food at a random position that is not in blocked cells.

        :param blocked: list of grid positions occupied by the snake
        """
        pos = self._random_position()
        while pos in blocked:
            pos = self._random_position()
        self.position = pos
