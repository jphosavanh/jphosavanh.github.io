# Fibonacci Term Calculator
# This program calculates the nth term in the Fibonacci sequence

def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    F₁ = 1, F₂ = 1, and F_n = F_{n-1} + F_{n-2} for n > 2
    """
    # Base cases
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1 or n == 2:
        return 1
    
    # For n > 2, calculate using the recurrence relation
    # Initialize the first two terms
    f1 = 1
    f2 = 1
    
    # Calculate each successive term up to n
    for i in range(3, n + 1):
        # The next Fibonacci number is the sum of the previous two
        next_fib = f1 + f2
        # Update values for the next iteration
        f1 = f2
        f2 = next_fib
    
    return f2

def main():
    # Prompt the user for the term number
    term = input("Which term? ")
    
    # Convert the input to an integer
    n = int(term)
    
    # Calculate and print the Fibonacci number
    result = fibonacci(n)
    print(result)

if __name__ == "__main__":
    main()
