term = int(input("Which term? "))
sum = 1
first = 1
second = 1
if term == 1:
    print(first)
elif term == 2:
    print(second)
else:
    for i in range(term - 2):
        sum = first + second
        second = first
        first = sum
    print(sum)
