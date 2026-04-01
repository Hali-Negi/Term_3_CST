"""
Assignment 1 - Snake Game
COMP 3522
Author: Hali Imanpanah
Student ID: A01363782
Date: Winter 2026
"""

import pygame
from food import Food
from pathfinding import BFSStrategy
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, GRID_COLS, GRID_ROWS, CELL_SIZE
from snake import Snake

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Game:
    """
    class Game:
    Main game engine responsible for:
    - Running the game loop
    - Handling user input
    - Updating game state
    - Rendering snake, food, and UI
    """

    def __init__(self):
        """
        Initializes pygame, window, and clock.
        """
        pygame.init()
        self._screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self._clock = pygame.time.Clock()

        self._running = True

        self._score = 0
        self._font = pygame.font.SysFont(None, 36)
        self._big_font = pygame.font.SysFont(None, 96)

        self._started = False
        self._game_over = False
        self._autopilot = False

        # Create the snake at the center of the grid
        self._snake = Snake((GRID_COLS // 2, GRID_ROWS // 2))

        # Create food
        self._food = Food()
        self._food.respawn(self._snake.body)

        self._pathfinding = BFSStrategy()

    def run(self):
        """
        Run the main game loop.
        """
        while self._running:
            self._handle_events()
            self._update()
            self._draw()
            self._clock.tick(FPS)

        pygame.quit()

    def _handle_events(self):
        """
        Handle pygame events and keyboard input.

        Supports:
        - Quit (close window)
        - Start game (SPACE)
        - Restart after game over (R)
        - Toggle autopilot mode (P)
        - Manual movement with arrow keys (when autopilot is off)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            if event.type == pygame.KEYDOWN:
                if self._game_over and event.key == pygame.K_r:
                    self._restart()
                    return

                if event.key == pygame.K_p:
                    self._autopilot = not self._autopilot
                    return

                if event.key == pygame.K_SPACE:
                    self._started = True
                    return

                if not self._autopilot:
                    if event.key == pygame.K_UP:
                        self._snake.set_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self._snake.set_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self._snake.set_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self._snake.set_direction(RIGHT)

    def _update(self):
        """
        Update game state
        - Execute autopilot pathfinding if enabled
        - Move the snake
        - Detect food collision and grow snake
        - Detect wall and self collisions
        - Update score and game over state
        """

        if not self._started or self._game_over:
            return

        if self._autopilot:
            path = self._pathfinding.find_path(
                start=self._snake.head,
                goal=self._food.position,
                blocked=set(self._snake.body[1:]),
                cols=GRID_COLS,
                rows=GRID_ROWS
            )

            if not path:
                self._autopilot = False
                return
            # Makes sure path has at least 2 cells.
            if len(path) > 1:
                next_cell = path[1]
                dc = next_cell[0] - self._snake.head[0]
                dr = next_cell[1] - self._snake.head[1]
                self._snake.set_direction((dc, dr))

        self._snake.move()

        # Check if snake head touches food
        if self._snake.head == self._food.position:
            self._snake.grow()
            self._food.respawn(self._snake.body)
            self._score += 1

        head_col, head_row = self._snake.head

        # wall collision
        if head_col < 0 or head_col >= GRID_COLS or head_row < 0 or head_row >= GRID_ROWS:
            self._game_over = True
            return

        # self collision(head bits body)
        if self._snake.head in self._snake.body[1:]:
            self._game_over = True
            return

    def _draw(self):
        """
        Render all game elements to the screen.

        Draws:
        - Background
        - Snake
        - Food
        - Score
        - Game over screen
        """
        self._screen.fill((0, 0, 0))
        self._draw_snake()
        self._draw_food()

        if self._game_over:
            self._draw_game_over()

        score_surf = self._font.render(f"Score: {self._score}", True, (255, 255, 255))
        self._screen.blit(score_surf, (10, 10))

        pygame.display.flip()

    def _draw_food(self):
        """
        Draw the food object on the screen.
        """
        col, row = self._food.position
        rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self._screen, (255, 0, 0), rect)

    # helper method
    def _draw_snake(self):
        """
        Draw all snake body segments on the screen.
        """

        # loops through every segment of snake's body.
        for col, row in self._snake.body:
            # converts grid position into actual pixel coordinates on the screen
            # Since CELL_SIZE = 20, a segment at grid position (5, 3) becomes a rectangle at pixel (100, 60) that is 20x20 pixels in size.
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self._screen, (0, 255, 0), rect)

    def _draw_game_over(self):
        """
        Display the game over message and restart instructions.
        """
        game_over_surf = self._big_font.render("GAME OVER", True, (255, 255, 255))
        restart_surf = self._font.render("Press R to restart", True, (255, 255, 255))

        go_rect = game_over_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        r_rect = restart_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70))

        self._screen.blit(game_over_surf, go_rect)
        self._screen.blit(restart_surf, r_rect)

    def _restart(self):
        """
        Reset the game state to initial conditions.

        - Recreate the snake
        - Respawn food
        - Reset score
        - Clear game over state
        """
        self._snake = Snake((GRID_COLS // 2, GRID_ROWS // 2))
        self._food.respawn(self._snake.body)
        self._score = 0
        self._started = True
        self._game_over = False
