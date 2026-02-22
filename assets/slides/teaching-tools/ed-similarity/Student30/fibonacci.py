n = int(input("Which term? "))
a, b = 1, 1
for _ in range(n - 2):
    a, b = b, a + b  
print(1 if n == 1 else b) 
