import numpy as np 
f=[1,1]
n=int(input('Which term? '))
for i in range(n):
    f.append(f[-1]+f[-2])
print(f[-3])
