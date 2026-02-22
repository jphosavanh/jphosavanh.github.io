n = input('Which term? ')
n = int(n)

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Enter a positive integer."
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(n - 2):
            a, b = b, a + b
        return b

print(fibonacci(n))

