import numpy as np
n = int(input('Which term? '))

seq = np.array([1,1])
for i in range(n-2):
    nex_num = int(seq[0] + seq[1])
    adding = np.array([nex_num])
    seq = np.concatenate([adding,seq])


print(seq[0])

