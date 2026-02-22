import numpy as np 
x = (int(input('Which term? ')))
seq = np.array([1,1])
for i in range(x-2):

    new_num = np.array([seq[0]+seq[1]]) 
    seq = np.concatenate([new_num, seq])
print(seq[0])
