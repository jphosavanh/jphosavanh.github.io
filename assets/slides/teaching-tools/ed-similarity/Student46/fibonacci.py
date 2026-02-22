import numpy as np 

num = int(input('Which term? '))

fib1 = 0
fib2 = 0
term = 0

for i in range(num):
    term = fib1 + fib2
    if i < 2:
        term = 1
    fib2 = fib1
    fib1 = term   
    
print(term)       
