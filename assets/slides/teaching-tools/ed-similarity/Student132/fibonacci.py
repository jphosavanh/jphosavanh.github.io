import numpy as np 
seq = np.array([1,1])
term = int(input("Which term? "))
for i in range(term-2):
    nextnum = np.array([seq[0]+seq[1]])
    seq = np.concatenate((nextnum,seq))
print(seq[0])
