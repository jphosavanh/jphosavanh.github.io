def fibonacci(n):
    if n <= 2:
        return 1
    f1, f2 = 1, 1
    for _ in range(3, n + 1):
        f1, f2 = f2, f1 + f2
    return f2

n_str = input("Which term? ")
n = int(n_str)

result = fibonacci(n)

print(result)

