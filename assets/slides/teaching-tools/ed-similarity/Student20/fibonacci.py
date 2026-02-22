n=int(input('Which term? '))
a=1
b=1
for i in range(n-1):
    c=a
    a=b
    b=c+b
print(a)

