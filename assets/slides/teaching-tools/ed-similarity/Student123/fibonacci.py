import numpy as np

val = int(input("Which term? "))

f1 = 1
f2 = 1

fibs = [f1, f2]
for i in range(val-2):
    fibs.append(fibs[-1]+fibs[-2])

print(fibs[-1])
