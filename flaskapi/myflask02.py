#!/usr/bin/python3
"""Intro to Flask"""

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to our Flask app!"
    
@app.route("/admin")
@app.route("/hello_admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hello {guesty} Guest"

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guesty = name))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
