def Fibo(n): 
    if n == 1:
        return 1
    if n == 2:
        return 1
    return Fibo(int(n)-1) + Fibo(int(n)-2)
n = int(input("Which term? "))
print(Fibo(n))


# def Fib(n):
#     a = 1
#     b = 1
#     c = None
#     for i in range(n):
#         if i <= 1:
#             pass 
#         else: 
#             c = a + b 
#             a = b 
#             b = c 
#     return c 
# print(Fib(n))
