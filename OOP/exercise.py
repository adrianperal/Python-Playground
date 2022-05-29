class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_valid(self):
        if self.side_a >= self.side_b + self.side_c or self.side_b >= self.side_a + self.side_c or self.side_c >= self.side_b + self.side_a:
            return False
        else:
            return True

    def classify(self):
        if self.side_a == self.side_b and self.side_b == self.side_c:
            return "Equilateral"
        elif self.side_a == self.side_b and self.side_b != self.side_c or self.side_a == self.side_c and self.side_c != self.side_b or self.side_b == self.side_c and self.side_c != self.side_a:
            return "Isosceles"
        elif self.side_a != self.side_b and self.side_b != self.side_c and self.side_c != self.side_a:
            return "Scalene"

    def compute_area(self):
        p = (self.side_a + self.side_b + self.side_c)/2
        return int(p*(p-self.side_a)*(p-self.side_b)*(p-self.side_c))

    def __str__(self):
        return f"Triangle with sides {self.side_a}, {self.side_b}, {self.side_c} has area {self.compute_area()}"

    def __lt__(self, other_triangle):
        return self.compute_area() < other_triangle.compute_area()


if __name__ == "__main__":
    triangle_list = []
    print("Enter first triangle:")
    triangle_list.append(Triangle(int(input("Enter side A: ")), int(
        input("Enter side B: ")), int(input("Enter side C: "))))
    print("Enter second triangle:")
    triangle_list.append(Triangle(int(input("Enter side A: ")), int(
        input("Enter side B: ")), int(input("Enter side C: "))))
    print(f"Triangle is valid: ", triangle_list[0].is_valid())
    print(f"Triangle Class: ", triangle_list[0].classify())
    print(f"Triangle Area: ", triangle_list[0].compute_area())
    print(f"Triangle is valid: ", triangle_list[1].is_valid())
    print(f"Triangle Class: ", triangle_list[1].classify())
    print(f"Triangle Area: ", triangle_list[1].compute_area())
    triangle_list.sort()
    print(f"Triangle{triangle_list[0].compute_area()} is smaller than {triangle_list[1].compute_area()}")
