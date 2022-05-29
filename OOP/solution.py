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

if __name__ == "__main__":
    triangle = Triangle(2, 2, 2)
    print(f"The triangle is valid? {triangle.is_valid()}")
    print(f"The triangle is {triangle.classify()} one")


