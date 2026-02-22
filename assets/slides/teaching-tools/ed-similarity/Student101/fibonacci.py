a=1
b=1

n= int(input('Which term? '))
for i in range(3,n):
    temp = b 
    b = a+b 
    a = temp 
print(b+temp)


