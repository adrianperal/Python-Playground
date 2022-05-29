def proper_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    return divisors

if __name__ == "__main__":
    n = int(input("Please provide an integer: "))
    print(proper_divisors(n))
