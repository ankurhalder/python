# Integer
a = 10
print(f"Variable 'a' is of type: {type(a)}")  # Output: <class 'int'>
print(f"Value of 'a': {a}")
print(f"Arithmetic operations with 'a': {a + 5}, {a - 3}, {a * 2}, {a / 3}")

# Float
b = 2.3
print(f"\nVariable 'b' is of type: {type(b)}")  # Output: <class 'float'>
print(f"Value of 'b': {b}")
print(f"Arithmetic operations with 'b': {b + 1.2}, {b - 0.3}, {b * 4}, {b / 2}")

# String
c = "hello world"
print(f"\nVariable 'c' is of type: {type(c)}")  # Output: <class 'str'>
print(f"Value of 'c': '{c}'")
print(f"String operations with 'c': {c.upper()}, {c.lower()}, {c[:5]}")

# Boolean
d = True
print(f"\nVariable 'd' is of type: {type(d)}")  # Output: <class 'bool'>
print(f"Value of 'd': {d}")
print(f"Logical operations with 'd': {not d}, {d and False}, {d or False}")

# List
e = [1, 2, 3, 4, 5, "hello", 2.3, True]
print(f"\nVariable 'e' is of type: {type(e)}")  # Output: <class 'list'>
print(f"Value of 'e': {e}")
print(f"List operations with 'e': {e[2]}, {len(e)}, {e + [6, 7]}, {e * 2}")

# Additional List operations
e.append("world")
e.remove(2)
print(f"Updated 'e' after append and remove: {e}")

# Checking membership in list
print(f"Checking membership: {'hello' in e}, {10 not in e}")

# Accessing list elements using negative indices
print(f"Accessing elements with negative indices: {e[-1]}, {e[-3]}")

# Slicing the list
print(f"Slicing the list 'e': {e[2:5]}, {e[:3]}, {e[4:]}")
