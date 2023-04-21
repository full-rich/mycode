#!/usr/bin/python3
import requests

simpson = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes").json()
with open("/home/student/mycode/pyvans/simpsons-py.txt", "w") as monorail:
    monorail.write(simpson[0]["quote"] + "\n" + simpson[0]["character"] + "\n")
