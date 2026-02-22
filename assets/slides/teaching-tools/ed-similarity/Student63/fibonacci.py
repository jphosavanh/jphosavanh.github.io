def Fibonacci_term(num):
    if num == 1 or num == 2:
        return 1
    else:
        return Fibonacci_term(num-1) + Fibonacci_term(num-2)

input = int(input("Which term? "))
print(Fibonacci_term(input))
