def fibonacci(n):
    if n <= 0:
        return "Invalid input. Enter a positive integer."
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

n = int(input("Which term? "))
print(fibonacci(n))
