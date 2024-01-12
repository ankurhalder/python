# A dictionary is a collection of key-value pairs.
# It is unordered, meaning that the items do not have a specific order.
# It is changeable, allowing you to add, modify, or remove items.
# It is indexed, meaning that you can access the items using their keys.
# The keys in a dictionary must be unique, but the values can be duplicates.

# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Accessing values using keys
print(my_dict["name"])  # Output: John

# Modifying values
my_dict["age"] = 35

# Adding new key-value pairs
my_dict["gender"] = "Male"

# Removing key-value pairs
del my_dict["city"]

# Checking if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary")

# Getting the number of key-value pairs
num_items = len(my_dict)

# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)

# Clearing the dictionary
my_dict.clear()

# Removing the dictionary
del my_dict

