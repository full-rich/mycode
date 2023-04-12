#!/usr/bin/env python3
"""Review of try and except logic"""

while True:
    try:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:     # openMode w can potentially overwrite stuff
            myfile.write("No problems with that file name.(This is new.)\n")
        break

    except:
        print("Error with that file name! Try again...")
                   