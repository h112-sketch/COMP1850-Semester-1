# Week 1.5, Session 1: Task 3
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



# Finally, add code here to demonstrate use of Point
point1 = Point(3, 4)
point2 = Point(6, 8)

print(f"Distance from origin: {point1.distance()}")
print(f"Distance between points: {point1.distance_to(point2)}")
