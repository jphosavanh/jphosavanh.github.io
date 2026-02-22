def fibonacci(n):
    # First two Fibonacci numbers are always 1
    if n == 1 or n == 2:
        return 1
    else:
        # Initialize the first two Fibonacci numbers
        a, b = 1, 1
        # Loop to calculate Fibonacci numbers
        for i in range(3, n + 1):
            a, b = b, a + b
        return b

# Ask for the term number
n = int(input('Which term? '))

# Output the corresponding Fibonacci number
print(fibonacci(n))

