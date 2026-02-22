import numpy as np

n = int(input('Which term? '))

seq = np.array([1,1])

for i in range (n-2):
    n = seq[0]+seq[1]
    next_num =np.array([n])

    seq = np.concatenate((next_num,seq))

print(seq[0])

