

class Dog:
    def __init__(self, name, breed, age, owner):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner

    def bark(self):
        print(f"Dog {self.name} is barking!")

    def __str__(self):
        return "Dog:" + self.name

    def __repr__(self):
        return f"Dog name: {self.name}, Breed: {self.breed}, Age: {self.age}, Owner: {self.owner}"

    def __lt__(self, other_dog):  # sort by age
         return self.age < other_dog.age


def dog_register():
    name = input("Enter dog name: ")
    breed = input("Enter dog breed: ")
    age = input("Enter dog age: ")
    owner = input("Enter dog owner: ")
    return Dog(name, breed, age, owner)


dog_list = [Dog("Nina", "Viralata", 5, "Adri"), Dog(
    "Murphy", "Pastor Aleman", 10, "Adri"), Dog("Bruno", "Chiguagua", 3, "Marcos")]
print(dog_list)
while True:
    x = input("Enter dog? (y/n) ")
    if x.lower() == "y":
        dog_list.append(dog_register())
        print(dog_list)
    else:
        # dog_list.sort(key=lambda x: x.age)  # sort by age using lambda
        dog_list.sort()  # sort by age using built-in sort
        print(dog_list)
        break
