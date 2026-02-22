def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# Ask the user for the term number
n = int(input("Which term? "))

# Print the corresponding Fibonacci number
print(fibonacci(n))

