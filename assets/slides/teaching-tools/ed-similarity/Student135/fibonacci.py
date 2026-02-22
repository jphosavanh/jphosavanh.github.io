# Ask for input
n = int(input("Which term? "))

# Define the first two Fibonacci numbers
if n == 1 or n == 2:
    fib = 1
else:
    # Start with F1 and F2
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    fib = b

# Output the result
print(fib)

