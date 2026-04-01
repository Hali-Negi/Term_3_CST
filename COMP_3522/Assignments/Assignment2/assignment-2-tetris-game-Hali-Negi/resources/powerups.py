import pygame


class PowerUp:
    def apply_effect(self, game, tetromino):
        pass


class NormalPowerUp(PowerUp):
    def apply_effect(self, game, tetromino):
        pass

class FreezePowerUp(PowerUp):
    # When a freeze tetromino locks into the grid, temporarily slow the game.
    # The drop speed is increased (pieces fall slower) and a timer is set
    # so the freeze effect lasts for a limited duration (3 seconds).
    def __init__(self, duration=3000):  # duration in ms, customizable
        self.duration = duration

    def apply_effect(self, game, tetromino):
        game.drop_speed = 600
        game.freeze_end_time = pygame.time.get_ticks() + self.duration
        pygame.time.set_timer(game.custom_event, game.drop_speed)



class BombPowerUp(PowerUp):
    def __init__(self, radius=1):
        self.radius = radius

    # Clear blocks around the bomb tetromino when it locks.
    def apply_effect(self, game, tetromino):
        # # 3×3 area around each occupied block
        # radius = 1

        for row_index, row in enumerate(tetromino.blocks[tetromino.state]):
            for col_index, block in enumerate(row):
                if block:
                    center_row = row_index + tetromino.row_offset
                    center_col = col_index + tetromino.col_offset

                    # clears a square area around each occupied block
                    for r in range(center_row - self.radius, center_row + self.radius + 1):
                        for c in range(center_col - self.radius, center_col + self.radius + 1):
                            if 0 <= r < 20 and 0 <= c < 10:
                                # if 0 <= r < len(game.grid.blocks) and 0 <= c < len(game.grid.blocks[0]):
                                game.grid.blocks[r][c] = 0