n = int(input("Which term? "))
F = [1,1]
for i in range(2,n):
    Fn = F[i-1]+F[i-2]
    F.append(Fn)

print(F[n-1])

