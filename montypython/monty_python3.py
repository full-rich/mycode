#!/usr/bin/env python3

round = 0
answer = " "

while round < 3 and (answer != "Brian" and answer != "Shrubbery"):
    round += 1 # increase round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer = answer.capitalize()
    if answer == "Brian": # logic to check if user gave correct answer"
        print("Correct!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian!")
    elif answer == "shrubbery":
        print("You gave the super secret answer!")
    else:               # if answer was wrong
        print("Sorry, Try again!")