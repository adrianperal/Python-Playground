def calculator(operand_1, operand_2, operator):
    if float(operand_1) and float(operand_2):
        operand_1 = float(operand_1)
        operand_2 = float(operand_2)
    else:
        raise TypeError("Please enter a number")
    if operator == "+":
        result = operand_1 + operand_2
    elif operator == "-":
        result = operand_1 - operand_2
    elif operator == "*":
        result = operand_1 * operand_2
    elif operator == "/" and operand_2 != 0:
        result = operand_1 / operand_2
    else:
        raise ZeroDivisionError("Invalid Input (divide by zero)")
    return result

if __name__ == "__main__":
    x = input("Enter first operand: ")
    y = input("Enter second operand: ")
    z = input("Enter operator: ")
    print("Calculating...")
    print("Result =",calculator(x, y, z)) # An example