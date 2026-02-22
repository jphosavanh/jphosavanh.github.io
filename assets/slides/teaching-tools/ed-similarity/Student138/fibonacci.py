def fibonacci(n):
    if n == 1 or n == 2:
        return 1  # The first two terms are 1
    a, b = 1, 1  # Initialize first two terms
    for _ in range(n - 2):
        a, b = b, a + b  # Compute next term
    return b

n = int(input("Which term? "))  # Read user input
print(fibonacci(n))  # Print the nth Fibonacci number

