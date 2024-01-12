# Method 1: Using `open` and `write` with explicit file closing
file = open('data/output.txt', mode='w')  # Open the file in write mode

try:
    file.write("Hello, World!\n")  # Write a line to the file
finally:
    file.close()  # Close the file

# Method 2: Using `with` statement for automatic file closing
with open('data/output.txt', mode='w') as file:
    file.write("Hello, World!\n")  # Write a line to the file

# Method 3: Writing multiple lines using `writelines`
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('data/output.txt', mode='w') as file:
    file.writelines(lines_to_write)  # Write multiple lines to the file

# Method 4: Appending to an existing file using `a` mode
with open('data/output.txt', mode='a') as file:
    file.write("This line is appended.\n")  # Append a line to the file

# Method 5: Using formatted string for writing data
name = "John"
age = 25
with open('data/output.txt', mode='w') as file:
    file.write(f"Name: {name}, Age: {age}\n")  # Write formatted string to the file

# Method 6: Writing binary data to a file
binary_data = b'\x48\x65\x6C\x6C\x6F'  # Hello in ASCII
with open('data/binary_output.bin', mode='wb') as binary_file:
    binary_file.write(binary_data)  # Write binary data to the file

# Method 7: Writing data using context managers for multiple files
with open('data/output1.txt', mode='w') as file1, open('data/output2.txt', mode='w') as file2:
    # Perform operations on file1 and file2 within this block
    file1.write("Data for file 1\n")
    file2.write("Data for file 2\n")

# Method 8: Using try-except for handling file writing errors
try:
    with open('protected/output.txt', mode='w') as file:
        file.write("Hello, World!\n")
except PermissionError:
    print("Permission error. Unable to write to the file.")

# Method 9: Writing CSV files using the csv module
import csv

data_to_write = [['Name', 'Age'], ['John', 25], ['Alice', 30]]
with open('data/output.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_to_write)

# Method 10: Using 'x' mode to create a new file (fails if the file already exists)
try:
    with open('data/new_file.txt', mode='x') as new_file:
        new_file.write("This is a new file.\n")
except FileExistsError:
    print("File already exists. Use a different file name.")

# Method 11: Writing data using a loop
data_to_write = ["Line 1", "Line 2", "Line 3"]
with open('data/output.txt', mode='w') as file:
    for line in data_to_write:
        file.write(line + '\n')  # Write each line to the file with a newline character

# Method 12: Using `flush` to force data to be written immediately
with open('data/output.txt', mode='w') as file:
    file.write("This data is written immediately.\n")
    file.flush()  # Force the data to be written to the file immediately

# Method 13: Writing formatted data using `format`
name = "Jane"
age = 22
with open('data/output.txt', mode='w') as file:
    file.write("Name: {}, Age: {}\n".format(name, age))

# Method 14: Writing JSON data to a file
import json

data_to_write = {'name': 'John', 'age': 25, 'city': 'New York'}
with open('data/output.json', mode='w') as json_file:
    json.dump(data_to_write, json_file, indent=2)

# Method 15: Using file positioning for seeking
with open('data/output.txt', mode='w') as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.seek(0)  # Move the file cursor to the beginning
    file.write("New Line 1\n")  # Overwrite the first line

# Method 16: Writing to a specific line in a file
line_number_to_replace = 2
replacement_line = "This is the new line"
with open('data/output.txt', mode='r+') as file:
    lines = file.readlines()
    lines[line_number_to_replace - 1] = replacement_line + '\n'
    file.seek(0)
    file.writelines(lines)

# Method 17: Writing data to a file using the `print` function
with open('data/output.txt', mode='w') as file:
    print("Line 1", file=file)
    print("Line 2", file=file)

# Method 18: Writing multiline strings using triple-quotes
multiline_data = """Line 1
Line 2
Line 3"""
with open('data/output.txt', mode='w') as file:
    file.write(multiline_data)

# Method 19: Using a custom separator in writelines
lines_to_write = ["Line 1", "Line 2", "Line 3"]
with open('data/output.txt', mode='w') as file:
    file.writelines('\n'.join(lines_to_write))

# Method 20: Writing data to a file using `write` and `print` combination
with open('data/output.txt', mode='w') as file:
    file.write("Line 1")
    print("Line 2", file=file)
    file.write("Line 3\n")

# Method 21: Writing a list of strings as CSV using `csv.writer`
data_to_write = [['Name', 'Age'], ['John', 25], ['Alice', 30]]
with open('data/output.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_to_write)

# Method 22: Using `w` mode to create a new file (overwrites existing file)
with open('data/new_file.txt', mode='w') as new_file:
    new_file.write("This is a new file.\n")
