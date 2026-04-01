from tabnanny import check

import pygame

from resources import ui
from resources.colors import Colors
from resources.command import Command
from resources.powerups import NormalPowerUp, FreezePowerUp, BombPowerUp



class Tetrominos:
    # def __init__(self):
    #     self.state = 0
    #     self.row_offset = 0
    #     self.col_offset = 3
    def __init__(self, power_up=None):
        self.state = 0
        self.row_offset = 0
        self.col_offset = 3
        self.power_up = power_up if power_up is not None else NormalPowerUp()

    def draw(self, screen, ui_x_offset = 0, ui_y_offset= 0):
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
                    pygame.draw.rect(
                        screen,
                        self.color,
                        (
                            (col_index + self.col_offset) * 30 + ui_x_offset,
                            (row_index + self.row_offset) * 30 + ui_y_offset,
                            30 - 1,
                            30 - 1,
                        ),
                    )

                    if isinstance(self.power_up, FreezePowerUp):
                        pygame.draw.rect(
                            screen,
                            Colors.YELLOW.value,
                            (
                                (col_index + self.col_offset) * 30 + ui_x_offset,
                                (row_index + self.row_offset) * 30 + ui_y_offset,
                                30 - 1,
                                30 - 1,
                            ),
                            2,
                        )
                    if isinstance(self.power_up, BombPowerUp):
                        pygame.draw.rect(
                            screen,
                            Colors.YELLOW.value,
                            (
                                (col_index + self.col_offset) * 30 + ui_x_offset,
                                (row_index + self.row_offset) * 30 + ui_y_offset,
                                30 - 1,
                                30 - 1,
                            ),
                            2,
                        )

    def update(self, command, grid, game):
        def out_of_boundaries():
            for row_index, row in enumerate(self.blocks[self.state]):
                for col_index, block in enumerate(row):
                    if block:
                        if (
                                row_index + self.row_offset > 19
                                or col_index + self.col_offset > 9
                                or col_index + self.col_offset < 0
                        ):
                            return True
            return False


        def check_for_completed_rows_and_clear(grid):
            number_of_cleared_rows = 0
            for row_index, row in enumerate(grid.blocks):
                    if all(row):
                        number_of_cleared_rows += 1
                        grid.blocks.pop(row_index   )
                        grid.blocks.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            return number_of_cleared_rows

        def lock_tetromino(grid, game):
            """
            carbon copy to tetromino into the grid
            """
            for row_index, row in enumerate(self.blocks[self.state]):
                for col_index, block in enumerate(row):
                    if block:
                      grid.blocks[row_index + self.row_offset ][
                          col_index + self.col_offset
                       ]= self.color

            number_of_cleared_rows =  check_for_completed_rows_and_clear(grid)

            # activate power-up effect for this tetromino
            self.activate_power_up(game)

            game.score += number_of_cleared_rows * 100

        def collides_with_other_tetrominos(grid):
            for row_index, row in enumerate(self.blocks[self.state]):
                for col_index, block in enumerate(row):
                    if block:
                        if grid.blocks[row_index + self.row_offset][col_index + self.col_offset]:
                            return True

            return False

        if command == Command.LEFT:
            self.col_offset -= 1
            if out_of_boundaries():
                self.col_offset += 1
            if collides_with_other_tetrominos(grid):
                self.col_offset += 1


        if command == Command.RIGHT:
            self.col_offset += 1
            if out_of_boundaries():
                self.col_offset -= 1
            if collides_with_other_tetrominos(grid):
                self.col_offset -= 1

        if command == Command.DOWN:
            self.row_offset += 1
            if out_of_boundaries():
                self.row_offset -= 1
                lock_tetromino(grid, game)
                game.spawn_new_tetromino()
                return

            if collides_with_other_tetrominos(grid ):
                self.row_offset -= 1

                if self.row_offset == 0:
                    game.game_over = True
                    print("Game Over!")

                lock_tetromino(grid, game)
                game.spawn_new_tetromino()


        if command == Command.UP:
            self.state = (self.state + 1) % len(self.blocks)
            if out_of_boundaries():
                self.state = (self.state - 1) % len(self.blocks)

    def activate_power_up(self, game):
        self.power_up.apply_effect(game, self)




class ZTetromino(Tetrominos):
    def __init__(self, power_up=None):
        super().__init__(power_up)
        self.color = Colors.BLUE.value

        self.blocks = [
            [
                [1, 1, 0],
                [0, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 0, 1],
                [0, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 1],
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [1, 0, 0],
            ],
        ]


class JTetromino(Tetrominos):
    def __init__(self, power_up=None):
        super().__init__(power_up)
        self.color = Colors.RED.value

        self.blocks = [
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 1],
                [0, 1, 0],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 1],
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 0],
            ],
        ]


class TTetromino(Tetrominos):
    def __init__(self, power_up=None):
        super().__init__(power_up)
        self.color = Colors.CYAN.value

        self.blocks = [
            [
                [0, 1, 0],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [0, 1, 0],
            ],
        ]


class LTetromino(Tetrominos):
    def __init__(self, power_up=None):
        super().__init__(power_up)
        self.color = Colors.GREEN.value

        self.blocks = [
            [
                [0, 0, 1],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 1],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [1, 0, 0],
            ],
            [
                [1, 1, 0],
                [0, 1, 0],
                [0, 1, 0],
            ],
        ]


class STetromino(Tetrominos):
    def __init__(self, power_up=None):
        super().__init__(power_up)
        self.color = Colors.PURPLE.value

        self.blocks = [
            [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 0, 1],
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [1, 1, 0],
            ],
            [
                [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0],
            ],
        ]


class OTetromino(Tetrominos):
    def __init__(self, power_up=None):
        super().__init__(power_up)
        self.color = Colors.YELLOW.value

        self.blocks = [
            [
                [1, 1],
                [1, 1],
            ]
        ]


class ITetromino(Tetrominos):
    def __init__(self, power_up=None):
        super().__init__(power_up)
        self.color = Colors.ORANGE.value

        self.blocks = [
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
            ],
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
            ],
            [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
            ],
        ]

