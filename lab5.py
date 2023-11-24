import math

class Colour:
    One = "RED"
    Two = "GREEN"
    Three = "BLUE"
#   RED = 1
#   GREEN = 2
#   BLUE = 3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    
class Polynom:
    def __init__(self, colour):
        self.points = []
        self.colour = colour

    def add_point(self, point):
        self.points.append(point)

    def perimeter(self):
        perimetr = 0
        for i in range(len(self.points)):
            x = self.points[(i+1) % len(self.points)].get_x() - self.points[i].get_x() # використовує % щоб переконатися, що індекс наступної точки не виходить за межі діапазону доступних індексів.
            y = self.points[(i+1) % len(self.points)].get_y() - self.points[i].get_y() # використовує % щоб переконатися, що індекс наступної точки не виходить за межі діапазону доступних індексів.
            perimetr += math.sqrt(x**2 + y**2)
        return perimetr                                                          
    
    def longest_diagonal(self):
        longest_diagonal = 0
        values = []
        for i in range(len(self.points)):
            for j in range(i + 2,len(self.points)): # (i + 2), щоб уникнути перевірки діагоналей між сусідніми точками.
                x = self.points[i].get_x() - self.points[j].get_x()
                y = self.points[i].get_y() - self.points[j].get_y() 
                diagonal = math.sqrt(x**2 + y**2)
                values.append(diagonal)
                longest_diagonal = max(values)
        return longest_diagonal

    def sort_by_x(self):
        self.points.sort(key=lambda point: point.get_x())

    def sort_by_y(self):
        self.points.sort(key=lambda point: point.get_y())

def main():
    poly = Polynom(Colour.One)

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
    print("Сортування точок за Х:")
    for point in poly.points:
        print(f"x = {point.get_x()}; y = {point.get_y()}")

    poly.sort_by_y()
    print("Сортування точок за Y:")
    for point in poly.points:
        print(f"x = {point.get_x()}; y = {point.get_y()}")
main()

