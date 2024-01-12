# Syntax:
# filter(function, iterable)

# Parameters:
# - function: A function that tests whether each element of an iterable is true or false.
# - iterable: An iterable object (e.g., list, tuple).

# Returns:
# An iterator containing the elements from the iterable for which the function returns true.

# Examples:

# 1. Basic Usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using lambda function to filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("1. Basic Usage:", list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# 2. Using a Named Function:
def is_positive(x):
    return x > 0

numbers = [-5, -2, 0, 3, 7, -1]
# Using a named function to filter positive numbers
positive_numbers = filter(is_positive, numbers)
print("2. Using a Named Function:", list(positive_numbers))  # Output: [3, 7]

# 3. Filtering Strings:
words = ["apple", "banana", "orange", "grape", "kiwi"]
# Using lambda function to filter words with more than 5 characters
long_words = filter(lambda x: len(x) > 5, words)
print("3. Filtering Strings:", list(long_words))  # Output: ['banana', 'orange']

# 4. Filtering None Values:
mixed_values = [1, None, "apple", 0, "orange", None, 7]
# Using lambda function to filter non-None values
non_none_values = filter(lambda x: x is not None, mixed_values)
print("4. Filtering None Values:", list(non_none_values))  # Output: [1, 'apple', 0, 'orange', 7]

# 5. Filtering with Multiple Conditions:
numbers = [10, 25, 3, -7, 0, 15, -2]
# Using lambda function to filter numbers between 5 and 20
filtered_numbers = filter(lambda x: 5 <= x <= 20, numbers)
print("5. Filtering with Multiple Conditions:", list(filtered_numbers))  # Output: [10, 15]

# 6. Removing Duplicates from a List:
duplicates = [1, 2, 2, 3, 4, 4, 5]
# Using lambda function to filter unique values
unique_values = filter(lambda x: duplicates.count(x) == 1, duplicates)
print("6. Removing Duplicates from a List:", list(unique_values))  # Output: [1, 3, 5]
