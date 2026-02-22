import numpy as np 

a1 = 1
a2 = 1

nn = input('Which term? ')

n = int(nn) - 2

for i in range(n):
    a3 = a2 + a1
    a1 = a2
    a2 = a3

print(a3)
