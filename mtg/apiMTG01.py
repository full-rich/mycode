#!/usr/bin/env python3
"""Accessing the MTG API with requests library"""

import requests

def main():
    """run time code"""

    # create resp, which is our request object
    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    print(resp.json().keys())
    print(resp.json())
    print(dir(resp))

if __name__ == "__main__":
    main()

