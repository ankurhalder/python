# Arithmetic operators
a = 10
b = 3

print("Addition:", a + b)        # Output: 13
print("Subtraction:", a - b)     # Output: 7
print("Multiplication:", a * b)  # Output: 30
print("Division:", a / b)        # Output: 3.333...
print("Floor Division:", a // b)  # Output: 3
print("Modulus:", a % b)          # Output: 1
print("Exponentiation:", a ** b)  # Output: 1000

# Comparison operators
x = 5
y = 10

print("Equal:", x == y)          # Output: False
print("Not Equal:", x != y)       # Output: True
print("Greater Than:", x > y)     # Output: False
print("Less Than:", x < y)        # Output: True
print("Greater Than or Equal:", x >= y)  # Output: False
print("Less Than or Equal:", x <= y)     # Output: True

# Logical operators
p = True
q = False

print("AND:", p and q)           # Output: False
print("OR:", p or q)              # Output: True
print("NOT:", not p)              # Output: False

# Membership operators
list_example = [1, 2, 3, 4, 5]

print("IN:", 3 in list_example)   # Output: True
print("NOT IN:", 6 not in list_example)  # Output: True

# Identity operators
m = [1, 2, 3]
n = [1, 2, 3]

print("IS:", m is n)             # Output: False
print("IS NOT:", m is not n)     # Output: True

# Assignment operators
x = 5
x += 2    # Equivalent to x = x + 2
print("Assignment Operator:", x)  # Output: 7

# Bitwise operators
p = 5   # Binary: 0101
q = 3   # Binary: 0011

print("Bitwise AND:", p & q)     # Output: 1 (Binary: 0001)
print("Bitwise OR:", p | q)      # Output: 7 (Binary: 0111)
print("Bitwise XOR:", p ^ q)     # Output: 6 (Binary: 0110)
print("Bitwise NOT:", ~p)        # Output: -6 (Binary: 1010)

# Ternary Operator
a = 5
b = 10
min_value = a if a < b else b
print("Ternary Operator:", min_value)  # Output: 5
