num = int(input("Which term? "))

a = [1, 1]

for i in range(2, num):
    a.append(a[i-1]+ a[i-2])

print(a[num - 1])

