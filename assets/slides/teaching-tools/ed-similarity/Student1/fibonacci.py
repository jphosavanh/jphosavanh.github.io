import  numpy  as  np
n=int(input('Which term? '))
if n==1 or n==2:
    print(1)
else:
    a=1
    b=1 
    for i in range(n-2):
        c=a+b
        a=b
        b=c
    print(b)
