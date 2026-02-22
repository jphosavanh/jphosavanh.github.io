import numpy as np 

term = int(input('Which term? '))
seq = np.array([1, 1])

for i in range(term - 2):
    n= seq[0] + seq[1]
    next_sum = np.array([n])

    seq = np.concatenate((next_sum, seq))

print(seq[0])
