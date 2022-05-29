from dataclasses import dataclass, field
from typing import List

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)  # default values for all arguments
class Student:
    name: str  
    age: int
    grades: List[float] = field(default_factory=list)
    score: float = 0.0 # default value    

def register_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grades = []
    for i in range(int(input("Enter number of grades: "))):
        grades.append(float(input("Enter grade: ")))
    score = sum(grades) / len(grades)
    return Student(name, age, grades, score)
student_1 = register_student()
print(student_1)