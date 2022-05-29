def evaluate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    except ValueError:
        print("Invalid input")
    except:
        print("Unknown error")

print(evaluate(input("Enter an expression: ")))