n = int(input("Which term? "))

fib = [1, 1]

for i in range(2, n):
    fib[i % 2] = fib[0] + fib[1]

print(f"{fib[(n-1) % 2]}")

