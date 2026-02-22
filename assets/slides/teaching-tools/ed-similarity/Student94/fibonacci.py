import numpy as np
# 'term' just names our code license
# 'int(xyz) converts answer to an integer
# 'input(xyz) displays our question
term = int(input('Which term? '))
# code below gives us our sequence (vector) with 2 starting variables 1,1...
a = np.array([1,1])
# code below lets us LOOP our code
# FOR must be lower case and has to finish with ":"
# the range is term because that is whatever number the user gives us, we want our code the input
# we put - 2 after term as we have the first 2 terms pre caculated, so our output will always show the first 2 numbers regardless of our input 
for i in range(term - 2):
# formula for the next number e.g a[0]=1 and a[1]=1 so n = 2 which is a[3]
    n = a[0]+a[1]
# code below must be as an array so Python can concate a vector with a vector;
# next_number = n would give an error
    next_number = np.array([n])
# code below 'lists' our variables one after the other
# np.concate joins a sequence of arrays along an existing axis.
    a = np.concatenate((next_number, a))
# below is out action code that will show
print(a[0])
