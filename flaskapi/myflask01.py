#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"
#app.add_url_rule("/hello", "hello", hello_world)

@app.route("/hello_darrin")
def hello_hutch():
    return "Hello Darrin"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)