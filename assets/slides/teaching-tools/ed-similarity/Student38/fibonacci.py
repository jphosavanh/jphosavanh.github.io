fib = int(input('Which term? '))
#for F2 = F0 + F1
#F0 = 0, F1 = 1, so F2 = 2

a = 0 #thats why a = 0
b = 1 
for i in range(1,fib):
    c = a + b
    a = b
    b = c

#Fn = c, Fn-1 = b, Fn-2 = a
#then once c is calculated, the numbers shift so that Fn turns to Fn-1, and Fn-1 turns to Fn-2: Thats why a = b and b =c after c is calculated
print(b)


#help came from "Python Program to Print the Fibonacci sequence" by GeeksForGeeks:
#https://www.geeksforgeeks.org/python-program-to-print-the-fibonacci-sequence/
