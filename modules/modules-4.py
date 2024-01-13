# 23. calendar Module
import calendar

# Display a calendar
cal = calendar.month(2024, 1)
print(cal)

# Check if a year is a leap year
is_leap = calendar.isleap(2024)
print(is_leap)  # Output: True

# 24. statistics Module (Basic statistical operations)
import statistics

data = [1, 2, 3, 4, 5]

# Mean
mean_value = statistics.mean(data)
print(mean_value)  # Output: 3.0

# Median
median_value = statistics.median(data)
print(median_value)  # Output: 3.0

# Standard deviation
std_deviation = statistics.stdev(data)
print(std_deviation)

# 25. zipfile Module (Working with ZIP archives)
import zipfile

# Create a ZIP file
with zipfile.ZipFile('my_archive.zip', 'w') as my_zip:
    my_zip.write('file1.txt')
    my_zip.write('file2.txt')

# Extract files from a ZIP file
with zipfile.ZipFile('my_archive.zip', 'r') as my_zip:
    my_zip.extractall('extracted_files')

# 26. platform Module (Accessing platform-specific information)
import platform

# Get the platform name
platform_name = platform.system()
print(platform_name)  # Output: Windows, Linux, Darwin, etc.

# Get the Python version
python_version = platform.python_version()
print(python_version)

# 27. webbrowser Module (Open a web browser)
import webbrowser

# Open a web page in the default browser
webbrowser.open('https://www.example.com')

# 28. turtle Module (Turtle graphics)
import turtle

# Draw a square using turtle graphics
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.done()

# 29. xml.etree.ElementTree Module (XML parsing)
import xml.etree.ElementTree as ET

# Parse an XML file
tree = ET.parse('example.xml')
root = tree.getroot()

# Access elements in the XML tree
for child in root:
    print(child.tag, child.attrib)

# 30. ctypes Module (Accessing C libraries)
import ctypes

# Load a dynamic link library (DLL)
my_lib = ctypes.CDLL('my_library.dll')

# Call a function from the library
result = my_lib.add(3, 4)
print(result)
# Install the required modules using:
# pip install pandas numpy matplotlib Flask sqlalchemy Django requests selenium pytest opencv-python scikit-learn tensorflow torch asyncio logging pyautogui fuzzywuzzy pillowfight networkx rich
