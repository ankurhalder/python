# List of favorite fruits
favorite_fruits = ["apple", "banana", "orange", "grape", "mango"]

# For loop using range
print("Using for loop with range:")
for i in range(10):
    print("Loop iteration", i)

# For loop iterating over a list
print("\nUsing for loop to iterate over a list:")
for fruit in favorite_fruits:
    print(fruit)

# While loop with a counter
print("\nUsing while loop with a counter:")
count = 0
while count < len(favorite_fruits):
    print(favorite_fruits[count])
    count += 1

# While loop with break statement
print("\nUsing while loop with break statement:")
count = 0
while True:
    if count >= len(favorite_fruits):
        break
    print(favorite_fruits[count])
    count += 1

# For loop with enumerate
print("\nUsing for loop with enumerate:")
for index, fruit in enumerate(favorite_fruits):
    print(f"Index {index}: {fruit}")

# Nested loops
print("\nUsing nested loops:")
for i in range(2):
    for j in range(3):
        print(f"({i}, {j})")

# Loop control statements
print("\nUsing loop control statements:")
for fruit in favorite_fruits:
    if fruit == "orange":
        continue  # Skip the rest of the code in this iteration
    print(fruit)

# Else clause in a loop
print("\nUsing else clause in a loop:")
for fruit in favorite_fruits:
    print(fruit)
else:
    print("No more fruits!")

# List comprehension
print("\nUsing list comprehension:")
squared_numbers = [num ** 2 for num in range(1, 6)]
print("Squared Numbers:", squared_numbers)
