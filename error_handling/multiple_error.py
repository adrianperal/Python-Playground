def evaluate(expression):
    try:
        return eval(expression)
    except (ZeroDivisionError, ValueError, TypeError, SyntaxError) as e:
        print("Something went wrong:", e)

print(evaluate(input("Enter an expression: ")))