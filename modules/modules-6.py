# 41. scikit-learn Module (Machine learning)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load iris dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# Create and train a k-nearest neighbors classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Make predictions
predictions = knn.predict(X_test)
print(predictions)

# 42. TensorFlow Module (Machine learning and deep learning)
import tensorflow as tf

# Define a simple neural network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 43. PyTorch Module (Machine learning and deep learning)
import torch
import torch.nn as nn

# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 44. asyncio Module (Asynchronous I/O)
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

# Run the asynchronous code
asyncio.run(main())

# 45. logging Module (Logging - Extended)
import logging

# Log to a file
logging.basicConfig(filename='my_log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 46. pyautogui Module (Automate mouse and keyboard)
import pyautogui

# Get the screen size
screen_size = pyautogui.size()
print(screen_size)

# Move the mouse
pyautogui.moveTo(100, 100, duration=1)

# 47. fuzzywuzzy Module (Fuzzy string matching)
from fuzzywuzzy import fuzz

# Compare strings
similarity = fuzz.ratio('python', 'pyhton')
print(similarity)  # Output: 92

# 48. pillowfight Module (Image processing - Extended)
from pillowfight import ncc

# Calculate normalized cross-correlation between two images
image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')
result = ncc(image1, image2)
print(result)

# 49. networkx Module (Graphs and networks)
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

# Draw the graph
nx.draw(G, with_labels=True)

# 50. rich Module (Rich text and formatting)
from rich.console import Console

# Create a rich console
console = Console()

# Print formatted text
console.print("[bold red]Hello[/bold red], [italic]World![/italic]")

# Install the required modules using:
# pip install pandas numpy matplotlib Flask sqlalchemy Django requests selenium pytest opencv-python scikit-learn tensorflow torch asyncio logging pyautogui fuzzywuzzy pillowfight networkx rich
