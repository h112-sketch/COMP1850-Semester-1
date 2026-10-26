# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given values for x and y.
        """
        # Add code here to check type and value of provided x & y,


        self.x = x
        self.y = y

    def distance(self):
        """
        Returns the distance of the point from the origin (0, 0).
        """
        # Add code here to calculate and return the distance from the origin
        return math.hypot(self.x, self.y)
    # Add distance() method here

    # Add distance_to() method here
    def distance_to(self, other):
        """
        Returns the distance from this point to another point.
        """
        if not isinstance(other, Point):
            raise TypeError("The other object must be a Point.")
        
        return self.distance() - other.distance() 
    # (This will need a parameter representing another point)


class Circle:
    """
    A Circle in 2D space, defined by a centre point and a radius.
    """

    def __init__(self, centre, radius):
        """
        Creates a Circle, given a centre Point and a radius.
        """
        if not isinstance(centre, Point):
            raise TypeError("Centre must be a Point object.")
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius < 0:
            raise ValueError("Radius cannot be negative.")

        self.centre = centre
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Returns the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
