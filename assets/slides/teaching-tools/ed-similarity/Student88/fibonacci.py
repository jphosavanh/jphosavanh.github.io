n = int(input('Which term? '))
f1 = 1
f2 = 1
f  = 0
for i in range (3, n+1):
    f= f1
    f1 = f2
    f2 = f + f2
print(f2)

