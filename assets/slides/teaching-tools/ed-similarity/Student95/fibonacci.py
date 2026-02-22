n = int(input('Which term? '));
if n == 1 or n == 2:
    print(1);
else:
    a,b=1,1;
    for i in range(n-2):  #loop run n-2 as the first two items are defined
        #a,b=b, a+b #a gets the value of b, then sum (a+b)
        temp = a;
        a = b;
        b = temp + b
    print(b)
