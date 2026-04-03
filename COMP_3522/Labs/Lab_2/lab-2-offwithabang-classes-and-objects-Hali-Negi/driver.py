"""
driver.py

Controls the asteroid simulation.
Creates asteroids, moves them once per second, and prints their state.
"""

import random          # Used to generate random numbers
import time            # Used to pause the program (sleep)
from datetime import datetime   # Used to get the current time

from asteroid import Asteroid   # Import the Asteroid class


class Controller:
    """
    Controls the simulation and stores all asteroids in a list.
    """

    def __init__(self):
        """
        Constructor.
        Creates 100 random Asteroid objects and stores them in a list.
        """

        # This list will hold all asteroid objects
        self.asteroids = []

        # Create 100 random asteroids
        for _ in range(100):
            # Random position inside a 100m cube
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            z = random.randint(0, 100)

            # Random velocity (0 to 5 metres per second)
            vx = random.randint(0, 5)
            vy = random.randint(0, 5)
            vz = random.randint(0, 5)

            # Random radius (1 to 4 metres)
            radius = random.randint(1, 4)

            # Create one asteroid object
            asteroid = Asteroid(x, y, z, vx, vy, vz, radius)

            # Add the asteroid to the list
            self.asteroids.append(asteroid)

    def simulate(self, seconds):
        """
        Moves every asteroid once per second for the given number of seconds.
        The simulation starts on the next whole second.
        """

        # Run the simulation for the requested number of seconds
        for _ in range(seconds):
            count = 1   # Used to number the asteroids in the output

            # Print the starting time
            print("Simulation Start Time:", datetime.now())
            print("\nMoving Asteroids!")
            print("-----------------\n")


            # Wait until the next whole second
            # (example: if time is 10.7 seconds, wait 0.3 seconds)
            now = datetime.now()
            wait = 1.0 - (now.microsecond / 1_000_000.0)
            if now.microsecond != 0:
                time.sleep(wait)

            # Loop through each asteroid in the list
            for asteroid in self.asteroids:
                # Move the asteroid and get its old position
                old_x, old_y, old_z = asteroid.move()

                # Print old and new position
                print(
                    f"Asteroid {count} Moved! Old Pos: {old_x}, {old_y}, {old_z} -> "
                    f"New Pos: {asteroid.x}, {asteroid.y}, {asteroid.z}"
                )

                # Print current position and velocity
                print(
                    f"Asteroid {count} is currently at {asteroid.x}, {asteroid.y}, {asteroid.z} "
                    f"and moving at {asteroid.vx}, {asteroid.vy}, {asteroid.vz} metres per second."
                )

                # Print circumference
                print(f"It has a circumference of {asteroid.get_circumference()}\n")

                count += 1


def main():
    """
    Main function that starts the simulation.
    """
    controller = Controller()     # Create the controller
    controller.simulate(5)        # Run the simulation for 1 second


if __name__ == "__main__":
    main()
