z = (1,) # defining tuple with one element
x = (1, 2, 3)
print(x[2])

def average(students):
    # TODO
    average = 0
    for student in students:
        average += student[2]
    return average / len(students)

    

def filter_average(students, average_grade):
    # TODO
    above_average = []
    for student in students:
        if student[2] > average_grade:
            above_average.append(student)
    return above_average

if __name__ == "__main__":
    # TODO
    student1 = ("John", "ID: 0", 8.4)
    student2 = ("Jane", "ID: 1", 9.2)
    student3 = ("Jack", "ID: 2", 7.8)
    student4 = ("Jill", "ID: 3", 8.6)
    student5 = ("Joe", "ID: 4", 9.0)
    my_class = [student1, student2, student3, student4, student5]
    average_grade = average(my_class)
    print(average(my_class))
    print(filter_average(my_class, average_grade))
