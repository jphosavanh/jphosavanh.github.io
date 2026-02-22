f1 = 1
f2 = 0
f= 0
index = int(input("Which term? "))
for i in range (index):
    f = f1+f2
    f1= f2
    f2 = f
print(f)
