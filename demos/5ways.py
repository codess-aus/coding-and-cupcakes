# Function to calculate the factorial of a number using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Method 2: Iterative approach using a for loop
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Method 3: Using while loop
def factorial_while(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


# Method 4: Using math.factorial() built-in function
import math

def factorial_builtin(n):
    return math.factorial(n)


# Method 5: Using reduce() from functools
from functools import reduce
import operator

def factorial_reduce(n):
    if n == 0:
        return 1
    return reduce(operator.mul, range(1, n + 1), 1)


# Test all implementations
if __name__ == "__main__":
    test_number = 5
    print(f"Calculating factorial of {test_number}:")
    print(f"1. Recursive: {factorial(test_number)}")
    print(f"2. Iterative: {factorial_iterative(test_number)}")
    print(f"3. While loop: {factorial_while(test_number)}")
    print(f"4. Built-in: {factorial_builtin(test_number)}")
    print(f"5. Reduce: {factorial_reduce(test_number)}")
