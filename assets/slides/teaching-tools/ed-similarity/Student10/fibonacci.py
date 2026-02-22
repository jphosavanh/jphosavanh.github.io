import numpy as np 

index = int(input("Which term? "))

seq = np.array([1, 1])

for i in range(index - 2): # -2 because we already have 1, 1 precalculated
    n = seq[0] + seq[1]
    new_num = np.array([n])

    seq = np.concatenate((new_num, seq)) # Reverses the array, making the indexes always right

print(seq[0])





# index = int(input("Which term? "))
# seq = np.array([1, 1])

# for element in range(index):
#     n = np.array([seq[::-1][0] + seq[::-1][1]])
#     seq = np.concatenate((seq, n))

# print(seq[index-1])




