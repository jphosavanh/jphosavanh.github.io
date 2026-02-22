import numpy as np
num = int(input('Which term? '))
seq = np.array([1,1])
for i in range (num-2):
    n = seq[-1] + seq[-2]
    next_sum = np.array ([n])
    seq = np.append (seq,n)

print (seq[-1])
