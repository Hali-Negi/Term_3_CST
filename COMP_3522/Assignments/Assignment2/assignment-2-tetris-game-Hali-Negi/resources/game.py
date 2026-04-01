import random

import pygame
from resources.command import Command
from resources.grid import Grid
from resources.tetrominos import *
from resources.ui import UI
from resources.tetromino_factory import NormalFactory, FreezeFactory, BombFactory



class Game:
    def __init__(self):
        pygame.init()

        # block size of 30x, 10 columns and 20 rows.
        self.screen = pygame.display.set_mode((500, 620))
        self. game_over = False
        self.score = 0
        self.drop_speed = 200
        self.freeze_end_time = 0
        self.custom_event = pygame.USEREVENT + 1

        # Objects
        self.grid = Grid()
        self.ui = UI()

        # Factory used to create tetrominos with different power-ups (Abstract Factory pattern)
        self.factory = NormalFactory()

        self.tetromino = random.choice(
            [
                self.factory.create_z(),
                self.factory.create_j(),
                self.factory.create_t(),
                self.factory.create_l(),
                self.factory.create_s(),
                self.factory.create_o(),
                self.factory.create_i(),
            ]
        )

        self.next_tetromino = random.choice(
            [
                self.factory.create_z(),
                self.factory.create_j(),
                self.factory.create_t(),
                self.factory.create_l(),
                self.factory.create_s(),
                self.factory.create_o(),
                self.factory.create_i(),
            ]
        )

    def run(self):
        running = True

        self.custom_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.custom_event, self.drop_speed)

        while running:
            command = None

            current_time = pygame.time.get_ticks()

            if self.freeze_end_time and current_time >= self.freeze_end_time:
                self.drop_speed = 200
                self.freeze_end_time = 0
                pygame.time.set_timer(self.custom_event, self.drop_speed)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_over =   False
                        self.__init__()

                    # Allow switching between factories during gameplay for testing power-up tetrominos
                    # F = FreezeFactory, B = BombFactory
                    if event.key == pygame.K_f:
                        self.factory = FreezeFactory()

                    if event.key == pygame.K_b:
                        self.factory = BombFactory()

                    if event.key == pygame.K_LEFT and not self.game_over:
                        command = Command.LEFT
                        print("LEFT")
                    if event.key == pygame.K_RIGHT and not self.game_over:
                        command = Command.RIGHT
                        print("RIGHT")
                    if event.key == pygame.K_DOWN and not self.game_over:
                        command = Command.DOWN
                        self.score  += 1
                        print("DOWN")
                    if event.key == pygame.K_UP and not self.game_over:
                        command = Command.UP
                        print("UP")
                if event.type == self.custom_event and not self.game_over:
                    command = Command.DOWN

            self.update(command)
            self.draw()

    def update(self, command):
        self.tetromino.update(command, self.grid,self )


    def draw(self):
        self.ui.draw(self.screen, self)
        self.grid.draw(self.screen, 10, 10)
        self.tetromino.draw(self.screen, 10, 10)
        pygame.display.update()

    def spawn_new_tetromino(self):
        self.tetromino = self.next_tetromino

        self.next_tetromino = random.choice(
            [
                self.factory.create_z(),
                self.factory.create_j(),
                self.factory.create_t(),
                self.factory.create_l(),
                self.factory.create_s(),
                self.factory.create_o(),
                self.factory.create_i(),
            ]
        )
