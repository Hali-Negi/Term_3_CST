# Assignment 1 - Snake Game 🐍

Design and implement a Snake game in Python.

The snake should eat food, grow clear of walls and itself, and avoid obstacles.

# Requirements

1. **Game Board and Display:**
   - Create a game board/grid where the snake will move.
   - Display the game board on the screen using `Pygame` graphical library.

1. **Snake Object:**
   - Create a snake object that consists of a series of linked segments.
   - Initialize the snake with a default length and position on the game board.
   - Implement methods for moving the snake in different directions (up, down, left, right).
   - Implement a method to check for collisions with walls or itself.
   - Increase the snake's length when it eats food.
   - Allow Snake to find the food using in an Auto-pilot mode. You may use a shortest path algorithm (e.g., [Breadth First Search Algorithm](https://www.youtube.com/watch?v=oDqjPvD54Ss&t=0s)) for the snake to find the food efficiently.
      - You may use a keyboard key to toggle between the manual and auto-pilot mode.
      - Allow your snake to consider future strategies to find the food. For example, you invest some time later on to allow the snake to find the food using the depth first search algorithm.

1. **Food Object:**
   - Create a food object that appears randomly on the game board.
   - Ensure the food doesn't appear inside the snake.

1. **Game Logic:**
   - Handle user input to control the snake's movement.
   - Update the game board with the snake's position and the location of the food.
   - Detect collisions between the snake and food.
   - Increase the player's score when the snake eats food.
   - End the game when the snake collides with the wall or itself.
   - Display the player's score on the screen.

1. **Game Loop:**
   - Implement a game loop that continuously updates the game state and redraws the display.
   - Control the game speed to make it playable.

1. **User Interface:**
   - Display game over message when the snake loses.
   - Provide a way to restart the game after it ends.

1. **Scoring:**
   - Keep track of the player's score based on the number of food items eaten.

Design and implement your Snake game using object-oriented programming principles you learned in Python. You'll likely have classes for the game board, snake, food, and the main game engine, among others, to encapsulate the game's logic and functionality.

# Marking Scheme

**1: Game Functionality (55 points)**

1. **Game Initialization (10 points)**
   - Properly initialize the game board, snake, and food objects.
   - Ensure the snake doesn't collide with itself or the wall at the start.
1. **Snake Movement (10 points)**
   - Implement smooth and responsive movement controls (up, down, left, right) or (W, S, A, D).
   - Handle collisions with the wall and snake's own body correctly.
1. **Food Generation and Consumption (10 points)**
   - Randomly generate food on the game board.
   - Detect of snake-food collisions.
   - Increase the snake's length upon eating food.
1. **Game Logic and State Management (10 points)**
   - Track the player's score.
   - Detect game over conditions.
   - Implement start functionality.
1. **Shortest Path Algorithm (15)**
   - Enable the snake to enable Auto-pilot mode to find the food.

**2: Code Quality and Structure (25 points)**

1. **Object-Oriented Design (10 points)**
   - Organizing code into classes and methods.
   - Demonstrate encapsulation and abstraction principles.
   - Break down the code into reusable and logical modules.
   - Minimize code duplication through proper modularization.
1. **Code Readability (15 points)**
   - Use meaningful variable and function names.
   - Maintain consistent code formatting and style.

**3: Class Diagram (10 points)**

- Draw a class diagram for the game. Attach the class diagram to the repo.

**4: SOLID Principles Compliance (10 points)**

- After you meet the game requirements above. Think about how you can improve the code by applying SOLID principles. Consider new requirements that may be added to the game in the future. For example, if you want to add a new feature to the game, how easy would it be to add it to the existing code? Would you need to change the existing code? Examples of new features include adding a new type of food, adding a new type of obstacle, or adding a new strategy for the autopolit. This is where SOLID principles come in handy. In the deliverable YT video, **Briefly** Discuss how SOLID principles are applied in the code.  
Here is an example of how you can apply SOLID principles to the Snake game:
To implement the auto-pilot mode for your snake game, you’ll need to handle different strategies for pathfinding, such as Breadth-First Search (BFS) and Depth-First Search (DFS). To achieve this, consider using a design approach that involves composition and inheritance. You can create an abstract base class or interface called `PathfindingStrategy` that defines a method like `find_path(start, goal)`. Then, create concrete classes like `BFSStrategy` and `DFSStrategy` that inherit from this base class and implement the specific pathfinding logic. In your Snake class, instead of tightly coupling it to a specific pathfinding algorithm, include an attribute that holds a reference to a `PathfindingStrategy` object. By doing this, you can easily switch between BFS and DFS (or even add new strategies in the future) without modifying the Snake class itself. This approach leverages composition to delegate the pathfinding responsibility, and inheritance to define a common strategy interface, aligning with object-oriented design principles to keep your code flexible and maintainable. Can you think of which SOLID principle is applied here?

**5: Demo and Testing**

1. **In-person demo during lab sessions (-40 points if not done)**
    - Demonstrate the game's functionality and features.
    - Ensure that the game runs smoothly without crashes.
    - Briefly discuss the code structure and design.
    - Discuss how SOLID principles are applied.
2. **Proper Commits (-20 points if not done)**
   - Use proper commit messages.
   - Commit often and regularly.
   - Keep commits small and focused.

**Total: 100 points**

