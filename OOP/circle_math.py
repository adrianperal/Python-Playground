import math


class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def __str__(self):
        str_print = f"Circle with radius {self.radius}"
        return str_print
    
    def area(self):
        area = self.radius ** 2 * math.pi
        return area
    
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
    def diameter(self):
        diameter = 2 * self.radius
        return diameter
    

radius = int(input("Enter radius: "))
circle_1 = Circle(radius)
print(f"Area: {circle_1.area()}, Perimeter: {circle_1.perimeter()}, Diameter: {circle_1.diameter()}")