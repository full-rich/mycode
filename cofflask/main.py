#!/usr/bin/python3
"""Simple Flask Application to take a coffee order"""

# import tools from Flask, render_template, url_for, Flask, ...

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

# create my Flask instance
app = Flask(__name__)

# get our user name; ENDPOINT 
@app.route("/")
@app.route("/enter_name")
def enter_name():
    return render_template("enter_name.html")



#  greet our user by name;  ENDPOINT
@app.route("/greet_user", methods = ["POST"])
def greet_user():
    if request.method == "POST":  # holds all the information when we click submit (POST in HTML)
        if request.form.get("user"):
            user = request.form.get("user")
        else:
            user = "default user"
    return render_template("greet_user.html", user=user)

# deliver their coffee order; ENDPOINT
@app.route("/serve", methods = ["POST"])
def server():
    if request.method == ["POST"]:
        if request.form.get("order"):
            order = request.form.get("order")
        else:
            order = "nothing."
    return render_template("serve.html", order=order)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
