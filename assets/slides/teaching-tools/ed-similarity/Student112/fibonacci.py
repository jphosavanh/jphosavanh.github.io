# Function to compute the Fibonacci number
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# Prompt the user for input
n = int(input("Which term? "))

# Print the nth Fibonacci number
print(fibonacci(n))
