import numpy as np

n = int(input('Which term? '))

seq = np.array([1, 1])

for i in range(n-2):
    next_num = np.array([seq[0] + seq[1]])
    seq = np.concatenate((next_num, seq))

print(seq[0])



