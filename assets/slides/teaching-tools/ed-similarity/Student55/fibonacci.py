import numpy as np 
f = np.array([1,1])
a = int(input("Which term? "))
for i in range(int(a)):
    newnum = f[i] + f[i+1]
    new = np.array([newnum])
    f = np.concatenate((f,new))
print(f[a-1])

