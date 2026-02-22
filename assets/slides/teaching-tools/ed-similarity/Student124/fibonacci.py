import numpy as numpy
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Ask the user for input
n = int(input("Which term? "))
print(fibonacci(n))

