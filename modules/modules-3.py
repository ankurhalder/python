# 15. subprocess Module (Run shell commands)
import subprocess

# Run a shell command
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)

# 16. itertools Module (Functional tools)
from itertools import permutations, combinations, product

# Permutations
perms = permutations([1, 2, 3])
print(list(perms))

# Combinations
combs = combinations([1, 2, 3], 2)
print(list(combs))

# Cartesian product
cart_prod = product([1, 2], ['a', 'b'])
print(list(cart_prod))

# 17. logging Module (Logging)
import logging

# Basic logging setup
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Log messages
logging.debug('This is a debug message.')
logging.info('This is an info message.')
logging.warning('This is a warning message.')
logging.error('This is an error message.')
logging.critical('This is a critical message.')

# 18. Pillow (PIL Fork) Module (Image processing)
from PIL import Image

# Open and display an image
img = Image.open('example.jpg')
img.show()

# Convert image to grayscale
gray_img = img.convert('L')
gray_img.show()

# Save the modified image
gray_img.save('example_gray.jpg')

# 19. smtplib Module (Sending emails)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'your_email@gmail.com'
receiver_email = 'recipient_email@gmail.com'
password = 'your_password'

# Create message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Subject of the email'

body = 'Body of the email'
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server and send email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)

# 20. hashlib Module (Cryptographic hash functions)
import hashlib

# Hashing passwords
password = 'my_secure_password'
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'salt', 100000)
print(hashed_password.hex())

# 21. pytz Module (Time zone support)
from datetime import datetime
import pytz

# Get current time in a specific time zone
tz = pytz.timezone('America/New_York')
current_time = datetime.now(tz)
print(current_time)

# 22. threading Module (Threading)
import threading

# Define a simple function to run in a thread
def print_numbers():
    for i in range(5):
        print(i)

# Create and start a thread
my_thread = threading.Thread(target=print_numbers)
my_thread.start()
my_thread.join()  # Wait for the thread to finish
# Install the required modules using:
# pip install pandas numpy matplotlib Flask sqlalchemy Django requests selenium pytest opencv-python scikit-learn tensorflow torch asyncio logging pyautogui fuzzywuzzy pillowfight networkx rich
