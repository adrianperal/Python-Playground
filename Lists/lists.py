x = "Adrian Antonio Peral" # String
a = [1, 2, 3, 4] # List of integers
b = [1, "two", 3, 4, True, 6] # List of different types of elements
c = [1, "hello", [True, 3, ["hey", 22]], 0] # nested list

print(c[2][2][1])

a.append(5) # Add an element to the end of the list
print(a)

def proper_divisors(n):
    # Your code here
    divisors = []
    divisor = n - 1
    while divisor > 0:
        if n % divisor == 0:
            divisors.append(divisor)
        divisor -= 1
    divisors.reverse()
    return divisors

if __name__ == "__main__":
    # Your code here
    print(proper_divisors(10))

# def proper_divisors(n):
#     divisors = []
#     for i in range(1, n):
#         if n % i == 0:
#             divisors.append(i)

#     return divisors

# if __name__ == "__main__":
#     n = int(input("Please provide an integer: "))
#     print(proper_divisors(n))