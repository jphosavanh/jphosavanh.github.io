import numpy as np 

n = int(input('Which term? '))
seq = np.array([1, 1])

for i in range(n - 2):
    m = seq[0] + seq[1]
    next = np.array([m])
    seq = np.concatenate((next, seq))

print(seq[0])
