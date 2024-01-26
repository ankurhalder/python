import os
from flask import Flask

os.environ['FLASK_APP'] = 'app.py'
os.environ['FLASK_ENV'] = 'development'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<b>My First Flask App.</b>"
