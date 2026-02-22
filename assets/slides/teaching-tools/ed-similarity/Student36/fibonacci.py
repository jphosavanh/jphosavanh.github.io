Fone = 1
Ftwo = 1



term = int(input("Which term? "))

if term == 1 or term == 2:
    print(base_1)

Fn = 0

for i in range(0,term-2):
    Fn = Fone + Ftwo
    Ftwo=Fone
    Fone = Fn


print(Fn)
