term = int(input('Which term? '))
import numpy as np 
seq = np.array([1,1])

for i in range (term-2):
    n = seq[0]+seq[1]
    nex_num = np.array([n])
    seq = np.concatenate((nex_num,seq))
print(seq[0])


