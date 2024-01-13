# map(function, iterable, ...)

# Parameters:
# - function: A function that takes one or more arguments.
# - iterable: One or more iterable objects (e.g., lists, tuples).

# Returns:
# An iterator that applies the given function to every item of the provided iterables (in parallel).

# Examples:

# 1. Basic Usage:
numbers = [1, 2, 3, 4, 5]
# Using lambda function to square each number in the list
squared = map(lambda x: x**2, numbers)
print("1. Basic Usage:", list(squared))  # Output: [1, 4, 9, 16, 25]

# 2. Multiple Iterables:
numbers = [1, 2, 3, 4, 5]
powers = [2, 3, 4, 5, 6]
# Using lambda function to raise each number to the corresponding power
result = map(lambda x, y: x**y, numbers, powers)
print("2. Multiple Iterables:", list(result))  # Output: [1, 8, 81, 1024, 15625]

# 3. Using a Named Function:
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
# Using a named function to square each number in the list
squared = map(square, numbers)
print("3. Using a Named Function:", list(squared))  # Output: [1, 4, 9, 16, 25]

# 4. Applying to Strings:
words = ["hello", "world", "python"]
# Using len function to get the length of each word in the list
lengths = map(len, words)
print("4. Applying to Strings:", list(lengths))  # Output: [5, 5, 6]

# 5. Using map with Multiple Functions:
numbers = [1, 2, 3, 4, 5]
# Using map to apply two lambda functions in sequence
result = map(lambda x: x * 2, map(lambda x: x + 1, numbers))
print("5. Using map with Multiple Functions:", list(result))  # Output: [4, 6, 8, 10, 12]

# 6. Handling Multiple Iterables of Different Lengths:
numbers = [1, 2, 3, 4, 5]
powers = [2, 3, 4]
# Stopping when the shorter iterable is exhausted
result = map(lambda x, y: x**y, numbers, powers)
print("6. Handling Multiple Iterables of Different Lengths:", list(result))  # Output: [1, 8, 81]
