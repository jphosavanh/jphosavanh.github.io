import numpy as np

seq = np.array([1, 1])

term = input("Which term? ")
term = int(term)

for i in range(term-2):
    n = seq[i+1] + seq[i]
    next_num = np.array([n])
    seq = np.concatenate((seq, next_num))

print(seq)
print(seq[term-1])

'''
element = input("Which term? ")

element = int(element)

f_n1 = 0
f_n2 = 0


for i in range(element):
    f_n = 1
    f_n2 = f_n1
    f_n1 = f_n
    f_n = f_n1 + f_n2

print(f_n)
    '''
