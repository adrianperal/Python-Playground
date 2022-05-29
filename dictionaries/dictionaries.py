my_list = [1, 2, "three", 4, 5]
tuple_to_list = tuple(my_list)  # type conversion works in either way
print(my_list)
print(type(tuple_to_list))
print(tuple_to_list)

print("---------------------------")

human = {"name": "John", "age": 35, "city": "New York", "alive": True}

print(human["name"])

print("---------------------------")

user = {
    "name": "John",
    "age": 35,
    "city": "New York",
    "gender": "male"
}
print(user["age"])
user["age"] = user["age"] + 1  # change value from user["age"] dictionarie
print(user)

print("---------------------------")

print("name" in user.keys())
print(35 in user.values())


print("---------------------------")

is_key = input("Enter key: ")
# if is_key in user.keys(): # check if key is in dictionarie using if statement
#     print("Key is in the dictionary")
# else:
#     print("Key is not in the dictionary")

if user.get(is_key, None):  # check if key is in dictionarie using get method
    print(f"Key: \'{is_key}\' is in the dictionary with value: {user[is_key]}")
else:
    print(f"Key: \'{is_key}\' is not in the dictionary")


print("---------------------------")

for key, value in user.items():
    print(f"Key: {key}, Value: {value}")
    
        