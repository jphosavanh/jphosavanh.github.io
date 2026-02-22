n = int(input("Which term? "))

a, b = 1, 1
for i in range(3, n + 1):
    a, b = b, a + b

print(b if n > 1 else 1)

