def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

# Ask the user for the term number with the updated prompt
n = int(input("Which term? "))

# Output the nth Fibonacci number without extra punctuation
print(f"{fibonacci(n)}")
