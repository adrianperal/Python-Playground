def new_sum(current_sum, value):
    result = current_sum
    try:
        result = current_sum + float(value)
    except ValueError:
        print("You enter an invalid, non-numeric value")

    return result

if __name__ == "__main__":
    user_input = input("Please enter an input: ")
    current_sum = 0
    while len(user_input) > 0:
        current_sum = new_sum(current_sum, user_input)
        print(f"Current sum: {current_sum}")
        user_input = input("Please enter an input: ")
