# Method 1: Using `open` and `readline` with explicit file closing
file = open('data/test.txt', mode='r')  # Open the file in read mode

try:
    data = file.readline()  # Read one line from the file
    print(data)  # Print the read data
finally:
    file.close()  #Note Close the file

# Method 2: Using `with` statement for automatic file closing
with open('data/test.txt', mode='r') as file:
    data = file.readline()  # Read one line from the file
    print(data)  # Print the read data

# Method 3: Reading all lines at once using `readlines`
with open('data/test.txt', mode='r') as file:
    all_lines = file.readlines()  # Read all lines from the file into a list
    for line in all_lines:
        print(line.strip())  # Print each line (strip removes trailing newline characters)

# Method 4: Iterating through lines using a for loop
with open('data/test.txt', mode='r') as file:
    for line in file:
        print(line.strip())  # Print each line (strip removes trailing newline characters)

# Method 5: Reading the entire file content using `read`
with open('data/test.txt', mode='r') as file:
    entire_content = file.read()  # Read the entire content of the file into a string
    print(entire_content)

# Method 6: Using context managers for multiple files
with open('data/file1.txt', mode='r') as file1, open('data/file2.txt', mode='r') as file2:
    # Perform operations on file1 and file2 within this block
    data_from_file1 = file1.readline()
    data_from_file2 = file2.readline()
    print(data_from_file1, data_from_file2)

# Method 7: Reading binary files
with open('data/binary_file.bin', mode='rb') as binary_file:
    binary_data = binary_file.read()  # Read the entire binary content
    print(binary_data)

# Method 8: Reading a specific number of characters from a file
with open('data/test.txt', mode='r') as file:
    partial_data = file.read(10)  # Read the first 10 characters from the file
    print(partial_data)

# Method 9: Using try-except for handling file reading errors
try:
    with open('nonexistent_file.txt', mode='r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found!")

# Method 10: Reading CSV files using the csv module
import csv

with open('data/data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
