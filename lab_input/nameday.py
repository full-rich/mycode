#!/usr/bin/env python3

#ask user to input name
def name():
    #gather string input from user
    first_name = input("Please enter your first name:")
    day = input ("Please enter the day of the week:")
    print(f"Hello, {first_name}! Happy {day}!")

name()