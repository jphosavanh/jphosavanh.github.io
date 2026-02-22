n = int(input("Which term? "))

f1, f2 = 1, 1
for i in range(n - 2):
    f1, f2 = f2, f2 + f1
print (f2)



