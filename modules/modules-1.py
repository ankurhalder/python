# 1. Math Module
import math

# Constants
pi = math.pi
e = math.e

# Basic operations
result = math.sqrt(25)
print(result)  # Output: 5.0

# Trigonometric functions
angle = math.radians(45)
sin_value = math.sin(angle)
print(sin_value)  # Output: 0.7071067811865475

# 2. Random Module
import random

# Generate a random integer
random_number = random.randint(1, 10)
print(random_number)

# Generate a random float
random_float = random.random()
print(random_float)

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

# 3. DateTime Module
from datetime import datetime

# Current date and time
current_time = datetime.now()
print(current_time)

# Format a date
formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# 4. JSON Module
import json

# Convert Python object to JSON string
data = {"name": "John", "age": 30, "city": "New York"}
json_data = json.dumps(data)
print(json_data)

# Convert JSON string to Python object
python_object = json.loads(json_data)
print(python_object)

# 5. OS Module
import os

# Get current working directory
current_directory = os.getcwd()
print(current_directory)

# List files in a directory
files_in_directory = os.listdir(current_directory)
print(files_in_directory)

# 6. Requests Module (for making HTTP requests)
import requests

# Make a GET request
response = requests.get("https://www.example.com")
print(response.text)

# 7. SQLite Module (for working with SQLite databases)
import sqlite3

# Connect to a database
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Execute SQL query
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
conn.commit()

# Close the connection
conn.close()
# Install the required modules using:
# pip install pandas numpy matplotlib Flask sqlalchemy Django requests selenium pytest opencv-python scikit-learn tensorflow torch asyncio logging pyautogui fuzzywuzzy pillowfight networkx rich
