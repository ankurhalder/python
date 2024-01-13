# 8. Collections Module
from collections import Counter, defaultdict, OrderedDict

# Counter - Count occurrences of elements in a list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(my_list)
print(counter)  # Output: Counter({4: 4, 3: 3, 2: 2, 1: 1})

# defaultdict - Default values for a dictionary
my_dict = defaultdict(int)
my_dict['a'] += 1
print(my_dict)  # Output: defaultdict(<class 'int'>, {'a': 1})

# OrderedDict - Dictionary that retains order of insertion
ordered_dict = OrderedDict()
ordered_dict['one'] = 1
ordered_dict['two'] = 2
print(ordered_dict)  # Output: OrderedDict([('one', 1), ('two', 2)])

# 9. CSV Module
import csv

# Writing to a CSV file
with open('example.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['John', 30, 'New York'])
    csv_writer.writerow(['Alice', 25, 'London'])

# Reading from a CSV file
with open('example.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)

# 10. re Module (Regular Expressions)
import re

# Search for a pattern in a string
text = "The price of a shirt is $20."
pattern = re.compile(r'\$\d+')
match = pattern.search(text)
if match:
    print(match.group())  # Output: $20

# 11. sys Module
import sys

# Command-line arguments
arguments = sys.argv
print(arguments)

# Exit the program with an error code
sys.exit(1)

# 12. argparse Module (Command-line argument parsing)
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
args = parser.parse_args()
result = sum(args.integers)
print(result)

# 13. urllib Module (URL handling)
from urllib import request

url = "https://www.example.com"
response = request.urlopen(url)
html_content = response.read()
print(html_content)

# 14. hashlib Module (Hash functions)
import hashlib

# MD5 hash
md5_hash = hashlib.md5(b"Hello, World!").hexdigest()
print(md5_hash)

# SHA-256 hash
sha256_hash = hashlib.sha256(b"Hello, World!").hexdigest()
print(sha256_hash)
# Install the required modules using:
# pip install pandas numpy matplotlib Flask sqlalchemy Django requests selenium pytest opencv-python scikit-learn tensorflow torch asyncio logging pyautogui fuzzywuzzy pillowfight networkx rich
