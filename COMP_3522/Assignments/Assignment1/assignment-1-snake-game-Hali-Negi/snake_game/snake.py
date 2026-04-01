"""
Assignment 1 - Snake Game
COMP 3522
Author: Hali Imanpanah
Student ID: A01363782
Date: 2026-02-09
"""

"""
Snake class:
Represents the snake entity in the game.
Responsible for:
- Storing snake body segments
- Managing movement direction
- Handling growth logic
"""
from typing import List, Tuple

GridPos = Tuple[int, int]


class Snake:
    """
    Models the Snake in the game.
    Attributes:
          _body (List[GridPos]): List of grid positions representing the snake.
          _direction (GridPos): Current movement direction.
          _grow_next (bool): Flag indicating whether the snake should grow on next move.
    """

    def __init__(self, start_pos: GridPos):
        """
        Initializes the snake with starting position start_pos.
        The snake starts with length 3 and moves to the right by default.

        :param start_pos: starting grid position of the snake head
        """

        col, row = start_pos

        self._grow_next = False

        self._body: List[GridPos] = [
            (col, row),
            (col - 1, row),
            (col - 2, row),
        ]

        # Default direction: moving right
        self._direction: GridPos = (1, 0)  # moving right by default

    @property
    def body(self) -> List[GridPos]:
        """
        Returns the snake body positions.

        Using .copy() preserves encapsulation and prevents
        external modification of internal state.
        """
        return self._body.copy()

    @property
    def head(self) -> GridPos:
        """
        Returns the snake head positions.(first element of body)
        """
        return self._body[0]

    def set_direction(self, direction: GridPos):
        """
        Update the snake's movement direction.

        :param direction: New movement direction as (col_delta, row_delta).
        """

        cur_col, cur_row = self._direction
        new_col, new_row = direction

        if (cur_col + new_col, cur_row + new_row) == (0, 0):
            return

        self._direction = direction

    def grow(self):
        """
        Set the grow flag so the snake increases

        its length on the next movement step.
        """

        self._grow_next = True

    def move(self):
        """
        Move the snake one grid cell in the current direction.

        - Adds a new head in the movement direction.
        - Removes the tail unless growth was triggered.
        """

        head_col, head_row = self.head
        dir_col, dir_row = self._direction

        new_head = (head_col + dir_col, head_row + dir_row)

        # insert new head
        self._body.insert(0, new_head)

        # remove tail only if not growing
        if self._grow_next:
            self._grow_next = False
        else:
            self._body.pop()
