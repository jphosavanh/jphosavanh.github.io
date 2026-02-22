a1 = 1
a2 = 1
term = int(input('Which term? '))
for a in range(term-2):
    a1 = a1 + a2
    a2 = a1 - a2
print(a1)
