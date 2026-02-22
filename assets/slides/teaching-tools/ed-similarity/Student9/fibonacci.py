x = (int)(input("Which term? "))

if x ==1:
    print(0)
elif x == 2:
    print(1)
else:
    a,b = 0,1
    for _ in range(2,x+1):
        a, b = b, a + b
    print(b)
