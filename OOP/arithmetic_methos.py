class Depth:
    def __init__(self, depth):
        self.depth = depth
    
    def __repr__(self) -> str:
        return f"Depth: {self.depth}"
    
    def __add__(self, other_box):
        return Depth(self.depth + other_box.depth)
    
    def __sub__(self, other_box):
        return Depth(self.depth - other_box.depth)
    
    def __mul__(self, other_box):
        return Depth(self.depth * other_box.depth)
    
    def __div__(self, other_box):
        return Depth(self.depth * other_box.depth)
    
    

box_1 = Depth(int(input("Enter Box 1 depth: ")))
box_2 = Depth(int(input("Enter Box 2 depth:")))
print("Combining boxes...")
box_3 = box_1 + box_2
print(f"Box 3 Depth: {box_3.depth}")