n = int(input('Which term? '))
a, b = 1, 1
for _ in range(n - 2):
    a, b = b, a + b

print(b)

