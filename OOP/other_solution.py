import math

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_valid(self):
        # Don't worry if you did something else, there many ways to do the same.
        if self.side_a + self.side_b <= self.side_c or self.side_a + self.side_c <= self.side_b or self.side_b + self.side_c <= self.side_a:
            return False

        return True

    def classify(self):
        # Don't worry if you did something else, there many ways to do the same.
        if self.side_a == self.side_b == self.side_c:
            return "Equilateral"
        elif self.side_a != self.side_b != self.side_c:
            return "Scalene"
        else:
            return "Isosceles"

    def __str__(self):
        return f"{self.classify()}({self.side_a}, {self.side_b}, {self.side_c})"

    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def __lt__(self, other_triangle):
        return self.area() < other_triangle.area()

if __name__ == "__main__":
    triangle1 = Triangle(2, 2, 2)
    print(f"{triangle1} with area {triangle1.area()}")

    triangle2 = Triangle(1, 1, 1)
    print(f"{triangle2} with area {triangle2.area()}")

    print()
    print(f"{triangle1} < {triangle2} ? {triangle1 < triangle2}")
    print(f"{triangle2} < {triangle1} ? {triangle2 < triangle1}")