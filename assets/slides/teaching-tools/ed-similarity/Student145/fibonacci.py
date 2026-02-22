import numpy as np

seq = np.array([1,1])

term = int(input("Which term? "))
for i in range(term - 2):  
    n = seq[0]+seq[1]
    next_num = np.array([n])
    seq = np.concatenate((next_num, seq))

print(seq[0])
