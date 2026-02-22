term = int(input("Which term? "))
f1 = 1
f2 = 1
for i in range(term - 2):
    f1, f2 = f2, f1 + f2
print(f2)
