import numpy as np

term = int(input("Which term? "))
seq = np.array([1, 1])

for i in range (term - 2):
    f_n = seq[0] + seq[1]
    next_num = np.array([f_n])
    seq = np.concatenate((next_num, seq))


print(seq[0])
