import numpy as np
try:
    term = int(input("Which term? "))
    if term < 3:
        print(1)
    else:
        fibonacci = np.array([1, 1])
        while len(fibonacci) < term:
            fibonacci = np.append(fibonacci,(fibonacci[-1] + fibonacci[-2]))
        print(fibonacci[-1])
except:
    print("That is not a valid term...")

