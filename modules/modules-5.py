# 31. pandas Module (Data manipulation and analysis)
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# 32. NumPy Module (Numerical operations)
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Perform operations on the array
mean_value = np.mean(arr)
print(mean_value)

# 33. Matplotlib Module (Plotting)
import matplotlib.pyplot as plt

# Create a simple plot
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# 34. Flask Module (Web framework)
from flask import Flask

app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run()

# 35. SQLAlchemy Module (Database ORM)
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a simple database model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Connect to the database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# 36. Django Module (Web framework)
# (Note: Django is a large framework and may require a separate file and project structure)

# 37. requests Module (HTTP requests)
import requests

# Make a GET request
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response.json()
print(data)

# 38. Selenium Module (Web automation)
from selenium import webdriver

# Open a browser window
driver = webdriver.Chrome()
driver.get('https://www.example.com')

# Perform actions (e.g., click a button)
button = driver.find_element_by_css_selector('button')
button.click()

# 39. pytest Module (Testing)
# (Note: Separate test files are recommended for pytest)

# 40. OpenCV Module (Computer Vision)
import cv2

# Read and display an image
image = cv2.imread('example_image.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Install the required modules using:
# pip install pandas numpy matplotlib Flask sqlalchemy Django requests selenium pytest opencv-python scikit-learn tensorflow torch asyncio logging pyautogui fuzzywuzzy pillowfight networkx rich
