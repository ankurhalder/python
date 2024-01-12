# List Comprehensions:
# ---------------------
# Syntax: [expression for item in iterable if condition]

# Examples:

# 1. Basic List Comprehension:
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print("1. Basic List Comprehension:", squared)
# Output: [1, 4, 9, 16, 25]

# 2. List Comprehension with Condition:
even_squares = [x**2 for x in numbers if x % 2 == 0]
print("2. List Comprehension with Condition:", even_squares)
# Output: [4, 16]

# 3. Nested List Comprehension:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("3. Nested List Comprehension:", flattened)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4. List Comprehension with If-Else:
parity = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print("4. List Comprehension with If-Else:", parity)
# Output: ['odd', 'even', 'odd', 'even', 'odd']


# Dictionary Comprehensions:
# ---------------------------
# Syntax: {key_expression: value_expression for item in iterable if condition}

# Examples:

# 5. Basic Dictionary Comprehension:
word_lengths = {"apple": 5, "banana": 6, "orange": 6, "kiwi": 4}
squared_lengths = {word: length**2 for word, length in word_lengths.items()}
print("5. Basic Dictionary Comprehension:", squared_lengths)
# Output: {'apple': 25, 'banana': 36, 'orange': 36, 'kiwi': 16}

# 6. Dictionary Comprehension with Condition:
even_squared_lengths = {word: length**2 for word, length in word_lengths.items() if length % 2 == 0}
print("6. Dictionary Comprehension with Condition:", even_squared_lengths)
# Output: {'banana': 36, 'orange': 36}

# 7. Dictionary Comprehension with If-Else:
word_types = {word: 'fruit' if word in ['apple', 'banana', 'orange'] else 'other' for word in word_lengths}
print("7. Dictionary Comprehension with If-Else:", word_types)
# Output: {'apple': 'fruit', 'banana': 'fruit', 'orange': 'fruit', 'kiwi': 'other'}


# Set Comprehensions:
# -------------------
# Syntax: {expression for item in iterable if condition}

# Examples:

# 8. Basic Set Comprehension:
unique_lengths = {len(word) for word in word_lengths}
print("8. Basic Set Comprehension:", unique_lengths)
# Output: {4, 5, 6}

# 9. Set Comprehension with Condition:
odd_lengths = {len(word) for word in word_lengths if len(word) % 2 != 0}
print("9. Set Comprehension with Condition:", odd_lengths)
# Output: {5}

# 10. Set Comprehension with If-Else:
word_types_set = {('fruit', word) if word in ['apple', 'banana', 'orange'] else ('other', word) for word in word_lengths}
print("10. Set Comprehension with If-Else:", word_types_set)
# Output: {('fruit', 'apple'), ('fruit', 'banana'), ('fruit', 'orange'), ('other', 'kiwi')}


# Generator Expressions:
# -----------------------
# Syntax: (expression for item in iterable if condition)

# Examples:

# 11. Generator Expression:
squares_generator = (x**2 for x in numbers)
print("11. Generator Expression:", list(squares_generator))
# Output: [1, 4, 9, 16, 25]

# 12. Generator Expression with Condition:
even_squares_generator = (x**2 for x in numbers if x % 2 == 0)
print("12. Generator Expression with Condition:", list(even_squares_generator))
# Output: [4, 16]

# 13. Generator Expression with If-Else:
parity_generator = ('even' if x % 2 == 0 else 'odd' for x in numbers)
print("13. Generator Expression with If-Else:", list(parity_generator))
# Output: ['odd', 'even', 'odd', 'even', 'odd']
