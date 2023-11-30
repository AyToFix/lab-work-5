"""This module contains classes for working with geometric figures in 2D space"""
import math
from enum import Enum

class Colour(Enum):
    """Class representing different colors"""
    ONE = "RED"
    TWO = "GREEN"
    THREE = "BLUE"

class Point:
    """Class representing a point in 2D space"""
    def __init__(self, x, y):
        """Initialize a point with given x and y coordinates"""
        self.x = x
        self.y = y

    def get_x(self):
        """Get the x-coordinate"""
        return self.x

    def get_y(self):
        """Get the y-coordinate"""
        return self.y

class Polynom:
    """Class representing a polygon with methods to calculate perimeter/longest diagonal"""
    def __init__(self, colour):
        """Initialize a polygon with a specified color"""
        self.points = []
        self.colour = colour

    def add_point(self, point):
        """Add a point to the polygon"""
        self.points.append(point)

    def perimeter(self):
        """Calculate the perimeter of the polygon"""
        perimeter = 0
        for i, _ in enumerate(self.points):
            x = self.points[(i+1) % len(self.points)].get_x() - self.points[i].get_x()
            y = self.points[(i+1) % len(self.points)].get_y() - self.points[i].get_y()
            perimeter += math.sqrt(x**2 + y**2)
        return perimeter

    def longest_diagonal(self):
        """Find and calculate the longest diagonal in the polygon"""
        longest_diagonal = 0
        values = []
        for i, _ in enumerate(self.points):
            for j in range(i + 2,len(self.points)):
                x = self.points[i].get_x() - self.points[j].get_x()
                y = self.points[i].get_y() - self.points[j].get_y()
                diagonal = math.sqrt(x**2 + y**2)
                values.append(diagonal)
                longest_diagonal = max(values)
        return longest_diagonal

    def sort_by_x(self):
        """Sort the points of the polygon by their x-coordinates."""
        self.points.sort(key=lambda point: point.get_x())

    def sort_by_y(self):
        """Sort the points of the polygon by their y-coordinates."""
        self.points.sort(key=lambda point: point.get_y())

def main():
    """Demonstrate the Polynom class"""
    poly = Polynom(Colour.ONE)

    poly.add_point(Point(0,0))
    poly.add_point(Point(2,4))
    poly.add_point(Point(3,4))
    poly.add_point(Point(0,2))

    perimeter = poly.perimeter()
    longest_diagonal = poly.longest_diagonal()

    print("Колір:", poly.colour)
    print("Периметр:", perimeter)
    print("Найдовша діагональ:", longest_diagonal)

    poly.sort_by_x()
    print("Сортування точок за x:")
    for point in poly.points:
        print(f"x = {point.get_x()}; y = {point.get_y()}")
    poly.sort_by_y()
    print("Сортування точок за y:")
    for point in poly.points:
        print(f"x = {point.get_x()}; y = {point.get_y()}")

if __name__ == "__main__":
    main()
