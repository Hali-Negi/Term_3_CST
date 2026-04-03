"""
asteroid.py

Defines the Asteroid class used in the asteroid simulation.
Each asteroid has a position, velocity, and size (radius).
"""

import math


class Asteroid:
    """
    Represents a single asteroid in 3D space.

    Stores the asteroid’s position, velocity, and size,
    and will later provide methods for moving and reporting its state.
    """

    def __init__(self, x, y, z, vx, vy, vz, radius):
        """
        Initialize a new Asteroid object.

        :param x: initial x-coordinate
        :param y: initial y-coordinate
        :param z: initial z-coordinate
        :param vx: velocity in the x direction
        :param vy: velocity in the y direction
        :param vz: velocity in the z direction
        :param radius: radius of the asteroid
        """

        # Position
        self.x = x
        self.y = y
        self.z = z

        # Velocity
        self.vx = vx
        self.vy = vy
        self.vz = vz

        # Size
        self.radius = radius

    def move(self):
        """
        Move the asteroid one second forward using its velocity.
        Returns the old position.
        """
        old_x = self.x
        old_y = self.y
        old_z = self.z

        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

        return old_x, old_y, old_z

    def get_circumference(self):
        """
        Return the circumference of the asteroid.
        Formula: C = 2 × π × radius
        """
        return 2 * math.pi * self.radius
