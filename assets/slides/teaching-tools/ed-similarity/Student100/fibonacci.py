import numpy as np

term = int(input("Which term? "))

f = np.array([1, 1])

for i in range(term - 2):
    n = f[-1] + f[-2]
    next_num = np.array([n])
    f = np.concatenate([f, next_num])

print(f[-1])
