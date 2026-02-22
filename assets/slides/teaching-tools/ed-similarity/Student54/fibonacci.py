user_input = int(input("Which term? "))
fib_list = [0, 1]
for i in range(2, user_input + 1):
    fib_list.append(fib_list[i - 1] + fib_list[i - 2])

print(fib_list[user_input])
