# Get user input
n = int(input("Which term? "))

# Compute Fibonacci sequence iteratively
a, b = 1, 1
for _ in range(n - 2):
    a, b = b, a + b

# Print the nth Fibonacci number
print(a if n == 1 else b)

