#!/url/bin/env python3
"""using dev keys to access apis"""

from pprint import pprint
import requests
import urllib.request
import json

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    nasacreds = "api_key=" + nasacreds.strip("\n")
    print(nasacreds)

    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)
    print(apodurlobj)
    apodread = apodurlobj.read()
    apod = json.loads(apodread.decode("utf-8"))

    print("\n\nConverted Python data")
    print(apod.keys())
    pprint(apod)
    #print(apod["title"] + "\n")
    #print(apod["date"] + "\n")
    #print(apod["explanation"] + "\n")
    #print(apod["url"])
    #print(dir(apodurlobj))

if __name__ == "__main__":
    main()