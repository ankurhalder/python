import os
from flask import Flask

os.environ['FLASK_APP'] = 'app.py'
os.environ['FLASK_ENV'] = 'development'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {"message": "Hello, World!"}

@app.route('/about')
def about():
    return {"message": "This is the about page"}

@app.route('/contact')
def contact():
    return {"message": "This is the contact page"}
