#!/usr/bin/env python3
"""print() - concatenate vs print a series of items"""

def main():
    # collect string input from the user
    user_input = input("Please enter an IPv4 address:")

    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)

    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)

    ## collect string input from the user
    vendor_name = input("Please enter the vendor name associated with the device:")
    ## the line below creates a single string that is passed to print
    print("You told me the device's vendor name is:", vendor_name)

main()
