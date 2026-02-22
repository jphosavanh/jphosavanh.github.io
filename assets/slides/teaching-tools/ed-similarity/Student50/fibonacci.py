import numpy as np
n = int(input("Which term? "))
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    fib = np.zeros(n, dtype=int)
    fib[0], fib[1] = 1, 1

    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n - 1]
print(fibonacci(n))


