from flask import Flask

app = Flask(__name__)

@app.route('/home')
def index():
    return ("Hello World!")

@app.route('/about')
def about():
    return ("About Page")