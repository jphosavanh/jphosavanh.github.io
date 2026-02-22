import numpy as np


# F(n) = F(n-1) + F(n-2)

seq = np.array([1,1])
next_num = np.array([seq[0]+seq[1]])
seq = np.concatenate((next_num,seq))

u = int(input('Which term? '))
for i in range (u-3):
    n = np.array([seq[0]+seq[1]])
    seq = np.concatenate((n, seq))
    
print (seq[0])
