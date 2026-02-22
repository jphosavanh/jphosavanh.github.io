term = int(input("Which term? "))
fibbonaci = [1,1]
for i in range(term):
    fibbonaci.append(fibbonaci[-1]+fibbonaci[-2])
print(fibbonaci[term-1])
