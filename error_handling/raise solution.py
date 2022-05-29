def calculator(operand_1, operand_2, operator):
    if operator not in ["+", "-", "/", "*"]:
        raise ValueError(f"Operator should either be +, -, /, or * but {operator} was given.")

    if type(operand_1) is str:
        if not operand_1.isnumeric():
            try:
                operand_1 = float(operand_1)
            except ValueError:
                raise TypeError("Both operands should be numeric values.")
        else:
            operand_1 = int(operand_1)
    if type(operand_2) is str:
        if not operand_2.isnumeric():
            try:
                operand_2 = float(operand_2)
            except ValueError:
                raise TypeError("Both operands should be numeric values.")
        else:
            operand_2 = int(operand_2)
    if type(operand_1) not in [int, float] or type(operand_2) not in [int, float]:
        raise TypeError("Both operands should be numeric values.")
    if operator == "/" and operand_2 == 0:
        raise ValueError("Second operand should not be zero when dividing.")

    return eval(f"{operand_1} {operator} {operand_2}")

if __name__ == "__main__":
    print(calculator("1a", 2.1, "+"))
