def fib(x):
    if ((x == 1) or (x ==2)):
        return 1
    return fib(x-1) + fib(x-2)


def main():
    x = int(input("Which term? "))
    f = fib(x)
    print(f)

if __name__ == "__main__":
    main()
