i: int = int(input("Which term? "))

if (i ==0 or i==1):
    print("1")
else:
    prev = 1
    cur = 1
    index = 0
    while index < i- 2:
        temp = cur
        cur += prev
        prev = temp
        index+= 1
    print(cur)
