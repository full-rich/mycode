#!/usr/bin/env python3
"""Using Requests to access an API"""

from pprint import pprint
import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    """run time code"""

    resp = requests.get(f"{API}sets").json()

    pprint(resp)

if __name__ == "__main__":
    main()

