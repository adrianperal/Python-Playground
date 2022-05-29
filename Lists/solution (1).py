def average(students):
    sum_of_grades = 0
    for name, student_id, grade in students:
        sum_of_grades += grade

    return sum_of_grades / len(students)

def filter_average(students, average_grade):
    filtered_students = []
    for name, student_id, grade in students:
        if grade > average_grade:
            filtered_students.append((name, student_id, grade)) # Creating a new tuple

    return filtered_students

if __name__ == "__main__":
    students = []
    for i in range(5):
        name = input(f"Please provide student's {i + 1} name: ")
        student_id = input(f"Please provide student's {i + 1} id: ")
        grade = float(input(f"Please provide student's {i + 1} grade: "))
        students.append((name, student_id, grade))
        print()

    average_grade = average(students)
    passing_students = filter_average(students, average_grade)

    print(f"Average grade is: {average_grade}.")

    for name, student_id, grade in passing_students:
        print(f"{name} ({student_id})")
