#!/usr/bin/python3
"""first API requests"""

import urllib.request # helps us get it - btw request isn't a function so don't use from import format
import json # helps us parse what we get back

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    groundctrl = urllib.request.urlopen(MAJORTOM)

    helmet = groundctrl.read()
    #print(type(helmet))

    helmet = json.loads(helmet.decode("utf-8"))
    #print(type(helmet))
    #print(helmet.keys())
    print(f"There are {helmet['number']} people in space")

    for astro in helmet['people']:
        print(f"{astro['name']} is on the craft {astro['craft']}")
        
    

if __name__ == "__main__":
    main()



