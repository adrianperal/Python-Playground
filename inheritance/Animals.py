class Animal:
    def __init__(self, name, breed, age, owner):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner

    def __str__(self):  
        return f"{self.name} is a {self.breed} and is {self.age} years old. Owner: {self.owner}\n"

    def __lt__(self, other_animal):
        return self.age < other_animal.age


class Cat(Animal):
    def __init__(self, name, breed, age, lifes_left, owner):
        super().__init__(name, breed, age, owner)
        self.lifes_left = lifes_left

    def meow(self):
        print(f"{self.name} says meow!")

    def how_many_lifes(self):
        print(f"{self.name} has {self.lifes_left} lifes left.")

    def __repr__(self):  # __repr__ is used to print the object
        return f"Cat({self.name},{self.breed},{self.age},{self.lifes_left},{self.owner})" # Cat(name, breed, age, lifes_left, owner)


class Dog(Animal):
    def bark(self):
        print(f"Dog {self.name} is barking!")

    def __repr__(self):  # __repr__ is used to print the object
        return f"Dog({self.name},{self.breed},{self.age},{self.owner})"  # Dog(name, breed, age, owner)

