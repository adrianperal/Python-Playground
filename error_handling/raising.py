def divide(x, y):
    if y == 0:
        raise ValueError(f"second parameter should not be 0, current value: {y}")
    return x / y

try:
    result = divide(10, 2)
except ValueError as e:
    print(e)
except ZeroDivisionError as e2:
    print(e2)
finally:
    print(result)