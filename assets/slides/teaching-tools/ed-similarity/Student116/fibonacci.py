a = 1
b = 1
for i in range(int(input("Which term? "))-1):
    a, b = b, a
    a += b
print(b)
