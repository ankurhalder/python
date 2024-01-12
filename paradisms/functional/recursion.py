
# Recursion:
# Recursion is a programming technique where a function calls itself in its own definition.

# Base Case:
# A base case is the condition under which the recursion stops. It prevents the function from calling itself indefinitely.

# Example: Factorial using Recursion
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)  # Output: 120

# Example: Sum of Natural Numbers using Recursion
def sum_natural_numbers(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    else:
        return n + sum_natural_numbers(n-1)

result = sum_natural_numbers(5)
print(result)  # Output: 15

# Example: Fibonacci Sequence using Recursion
def fibonacci(n):
    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(6)
print(result)  # Output: 8

# Memoization:
# Memoization is a technique to optimize recursive functions by storing and reusing previously computed results.

# Example: Fibonacci Sequence with Memoization
def fibonacci_memo(n, memo={}):
    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Check if result is already memoized
    elif n in memo:
        return memo[n]
    # Recursive case
    else:
        # Memoize the result
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        return memo[n]

result = fibonacci_memo(6)
print(result)  # Output: 8

# Tail Recursion:
# Tail recursion is a special case where the recursive call is the last operation in the function.

# Example: Tail Recursive Factorial
def factorial_tail_recursive(n, accumulator=1):
    # Base case
    if n == 0 or n == 1:
        return accumulator
    # Tail recursive case
    else:
        return factorial_tail_recursive(n-1, n*accumulator)

result = factorial_tail_recursive(5)
print(result)  # Output: 120

# Pros and Cons of Recursion:

# Pros:
# - Elegance: Recursive solutions can be elegant and closely mirror the mathematical description of a problem.
# - Readability: Recursive solutions can be more readable for certain problems.

# Cons:
# - Memory Usage: Recursive calls consume additional memory due to the call stack.
# - Stack Overflow: Excessive recursion can lead to a stack overflow error.
# - Performance: Recursive solutions may not be as performant for certain problems.

# Tips for Using Recursion:

# 1. Define a clear base case to stop the recursion.
# 2. Ensure progress towards the base case in each recursive call.
# 3. Be cautious about memory usage and potential stack overflow.
# 4. Consider using memoization for optimization.

# Conclusion:
# Recursion is a powerful technique but should be used judiciously based on the problem requirements and constraints.
