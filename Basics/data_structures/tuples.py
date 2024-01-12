# Creating a tuple
my_tuple = ("hi", 1, 4.5, True, [1, 2, 3], (1, 2, 3), {"a": 1, "b": 2, "c": 3})

# Printing the type of my_tuple
print(type(my_tuple))

# Counting the number of occurrences of "hi" in my_tuple
count_hi = my_tuple.count("hi")
print(f"Number of occurrences of 'hi': {count_hi}")

# Finding the index of [1, 2, 3] in my_tuple
index_list = my_tuple.index([1, 2, 3])
print(f"Index of [1, 2, 3]: {index_list}")

# Iterating over each element in my_tuple and printing it
for element in my_tuple:
    print(element)

# Accessing elements of a tuple using indexing
first_element = my_tuple[0]
second_element = my_tuple[1]
print(f"First element: {first_element}")
print(f"Second element: {second_element}")

# Slicing a tuple
sliced_tuple = my_tuple[2:5]
print(f"Sliced tuple: {sliced_tuple}")

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(f"Concatenated tuple: {concatenated_tuple}")

# Checking if an element exists in a tuple
element_exists = "hi" in my_tuple
print(f"Does 'hi' exist in the tuple? {element_exists}")

# Getting the length of a tuple
tuple_length = len(my_tuple)
print(f"Length of the tuple: {tuple_length}")
