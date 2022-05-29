def new_sum(current_sum, value):
    try:
        current_sum = int(current_sum)
        value = int(value)
        if current_sum is int and value is int:
            return current_sum + value
        current_sum = float(current_sum)
        value = float(value)
        return current_sum + value
    except (ValueError, TypeError, SyntaxError) as e:
        print("Something went wrong: ", e)
    return current_sum

if __name__ == "__main__":
    user_input = input("Enter a number: ")
    current_sum = user_input
    while user_input != "":
        value = input("Enter another number: ")
        if value != "":
            current_sum = new_sum(current_sum, value)
            print(f"Result: {current_sum}")
        user_input = value
        