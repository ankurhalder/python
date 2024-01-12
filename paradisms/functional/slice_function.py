# Syntax:
# slice(start, stop, step)

# Parameters:
# - start: Starting index of the slice (inclusive).
# - stop: Ending index of the slice (exclusive).
# - step: Step size for slicing (optional, default is 1).

# Examples:

# 1. Basic slicing:
original_list = [0, 1, 2, 3, 4, 5]
# Extract elements from index 1 to 3 (exclusive)
sliced_list = original_list[slice(1, 4)]
print("1. Basic slicing:", sliced_list)  # Output: [1, 2, 3]

# 2. Using slice with step:
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Extract elements from index 1 to 8 with a step of 2
sliced_list = original_list[slice(1, 8, 2)]
print("2. Using slice with step:", sliced_list)  # Output: [1, 3, 5, 7]

# 3. Slice shorthand:
original_list = [0, 1, 2, 3, 4, 5]
# Equivalent to original_list[1:4]
sliced_list = original_list[1:4]
print("3. Slice shorthand:", sliced_list)  # Output: [1, 2, 3]

# 4. Omitting start or stop:
original_list = [0, 1, 2, 3, 4, 5]
# Same as original_list[None:3]
sliced_list = original_list[:3]
print("4. Omitting start or stop:", sliced_list)  # Output: [0, 1, 2]

# 5. Negative indices:
original_list = [0, 1, 2, 3, 4, 5]
# Extract the last three elements
sliced_list = original_list[slice(-3, None)]
print("5. Negative indices:", sliced_list)  # Output: [3, 4, 5]

# 6. Using slice in strings:
original_string = "Hello, World!"
# Extract the substring from index 7 to 11
sliced_string = original_string[slice(7, 12)]
print("6. Using slice in strings:", sliced_string)  # Output: World
