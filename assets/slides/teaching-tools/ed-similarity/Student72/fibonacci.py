import numpy as np
n = int(input('Which term? '))
seq = np.array([1,1])
for i in range(n-2):
   next_number = seq[0]+seq[1]

   next_num = np.array([next_number])
    
   seq =np.concatenate((next_num,seq))
    

print(next_number)
