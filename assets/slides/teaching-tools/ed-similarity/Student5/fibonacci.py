usr_index = int(input("Which term? "))
a = 1
b = 1
for i in range (usr_index):
    if (usr_index == 0 or usr_index == 1):
        print(1)
    else:
        if (i >= 2):
            a += b
            b = a - b
print(a)
