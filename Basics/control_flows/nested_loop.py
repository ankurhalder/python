import time

# Start measuring time
start_time = time.time()

# Nested loops
# Example 1: Nested for loops
for i in range(3):
    for j in range(2):
        print(f"Outer loop: {i}, Inner loop: {j}")

# Example 2: Nested while loops
x = 0
while x < 3:
    y = 0
    while y < 2:
        print(f"Outer loop: {x}, Inner loop: {y}")
        y += 1
    x += 1

# Measure and print elapsed time
elapsed_time = time.time() - start_time
print("--- %s seconds ---" % elapsed_time)
