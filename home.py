from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hey_there")

def hey_there():
    return "<p>my name is khan, World!</p>"

@app.route("/okay")
def okay():
     return "<p>this is me , and i am me!</p>"






