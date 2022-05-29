from Animals import Cat, Dog


def dog_register():
    name = input("Enter dog name: ")
    breed = input("Enter dog breed: ")
    age = int(input("Enter dog age: "))
    owner = input("Enter dog owner: ")
    return Dog(name, breed, age, owner)


def cat_register():
    name = input("Enter cat name: ")
    breed = input("Enter cat breed: ")
    age = int(input("Enter cat age: "))
    lifes_left = int(input("Enter cat lifes left: "))
    owner = input("Enter cat owner: ")
    return Cat(name, breed, age, lifes_left, owner)


dog_list = [
    Dog("Nina", "Viralata", 5, "Renata"),
    Dog("Murphy", "Pastor Aleman", 10, "Adri"),
]
print("\nDogs:")
for i in dog_list:
    print(i, end="")

cat_list = [
    Cat("Berni", "Siames-cabeludo", 16, 8, "Adri"),
    Cat("Papito", "Semi-Siames", 3, 4, "Adri"),
]
print("\nCats:")
for i in cat_list:
    print(i, end="")

while True:
    x = input("Enter letter [D] for dog or [C] for cat, (anything else to exit): ")
    if x.lower() == "d":
        dog_list.append(dog_register())
    elif x.lower() == "c":
        cat_list.append(cat_register())
    else:
        # dog_list.sort(key=lambda x: x.age)  # sort by age using lambda
        dog_list.sort()  # sort by age using built-in sort
        cat_list.sort()  # sort by age using built-in sort
        print("\nDogs:")
        for i in dog_list:
            print(i, end="")
        print("\nCats:")
        for i in cat_list:
            print(i, end="")
            print(f"and has {i.lifes_left} lifes left.")
        break
