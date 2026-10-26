# Week 1.5, Session 1: Task 4

import geometry

point = geometry.Point(0, 0)
circle = geometry.Circle(point, 5)

print(f"Area of the circle: {round(circle.area(), 2)}")
print(f"Perimeter of the circle: {round(circle.perimeter(), 2)}")

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
