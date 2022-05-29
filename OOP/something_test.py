class Human:
    def __init__(self, f_name, l_name):  # Constructor
        self.first_name = f_name
        self.last_name = l_name

    def list_people(self):  # Method
        print(f"Human: {self.first_name} {self.last_name}")


x = int(input("How many people are there: "))
population = []
for i in range(x):
    a = input("\nEnter first name: ")
    b = input("Enter last name: ")
    population.append(Human(a, b))  # Create an instance of the class on a list
print("\nHuman list:\n")
for i in range(x):
    population[i].list_people()  # Call the method on the list
