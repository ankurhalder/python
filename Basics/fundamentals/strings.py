# String methods
text = "   Python Programming   "
print(text.strip())            # Output: "Python Programming"
print(text.lower())            # Output: "   python programming   "
print(text.upper())            # Output: "   PYTHON PROGRAMMING   "
print(text.replace("Python", "Java"))  # Output: "   Java Programming   "
print(text.find("Programming"))         # Output: 9 (index of the first occurrence)
print(text.count("o"))                  # Output: 2 (number of occurrences)

# String formatting
name = "Alice"
age = 25
print("Hello, {}! You are {} years old.".format(name, age))
# Output: "Hello, Alice! You are 25 years old."

# f-string formatting (Python 3.6 and later)
print(f"Hello, {name}! You are {age} years old.")
# Output: "Hello, Alice! You are 25 years old."

# Joining strings with join()
languages = ["Python", "Java", "C++"]
joined_languages = ", ".join(languages)
print("Programming languages: " + joined_languages)
# Output: "Programming languages: Python, Java, C++"

# Splitting strings with split()
sentence = "This is a sample sentence."
words = sentence.split()
print(words)
# Output: ['This', 'is', 'a', 'sample', 'sentence.']

# Checking string properties
is_alpha = text.isalpha()          # False (due to spaces)
is_digit = text.isdigit()          # False
is_whitespace = text.isspace()     # False
is_title_case = text.istitle()     # True (each word starts with a capital letter)

# Checking string presence
contains_python = "Python" in text  # True

# String interpolation (Python 3.6 and later)
language = "Python"
version = 3.9
print(f"The latest version of {language} is {version}.")
# Output: "The latest version of Python is 3.9."
