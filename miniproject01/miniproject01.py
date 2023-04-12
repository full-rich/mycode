#!/usr/bin/env python3
"""This program will allow a user to select from a list of 3 states and generate at least two road trip itineraries from the selected state"""

def main():
    cont_loop = True
    while cont_loop == True:
        states = {
            "CA": "California",
            "NV": "Nevada",
            "OR": "Oregon",
        }
        states_long = states.values()
        print("The states to choose from include", states["CA"], ",", states["NV"], ", and", states["OR"])
        
        # have the user input a state they want to travel to
        sel_state = input("Please input which state you would like to travel to: ") 
                
        # capitalize state name
        sel_state = sel_state.title()

        # loop through user's selected state and output itinerary
        if sel_state == 'California':
            calif_itin = {
                "Itinerary 1" : "Los Angeles - Monterey - San Francisco",
                "Itinerary 2" : "San Diego - Mammoth - Lake Tahoe"
            }
            for itinerary, route in calif_itin.items():
                print(itinerary, route)
            print("Would you like to select a new state?")
            cont_loop = input("Y/N: ")
            cont_loop = cont_loop.lower()
            if cont_loop == "y":
                cont_loop = True
            else:
                break
        elif sel_state == 'Nevada':
            nev_itin = {
                "Itinerary 1" : "Las Vegas - Reno - Lake Tahoe",
                "Itinerary 2" : "Winnemuca - Reno - Las Vegas"
            }
            for itinerary, route in nev_itin.items():
                print(itinerary, route)
            print("Would you like to select a new state?")
            cont_loop = input("Y/N: ")
            cont_loop = cont_loop.lower()
            if cont_loop == "y":
                cont_loop = True
            else:
                break
        elif sel_state == 'Oregon':
            or_itin = {
                "Itinerary 1" : "Baker City - Portland - Medford",
                "Itinerary 2" : "Burns - Klamath Falls - Medford"
            }
            for itinerary, route in or_itin.items():
                print(itinerary, route)
            print("Would you like to select a new state?")
            cont_loop = input("Y/N: ")
            cont_loop = cont_loop.lower()
            if cont_loop == "y":
                cont_loop = True
            else:
                break
        else:
            print("Your input didn't match any of the above states, would you like to continue?")
            cont_loop = input("Y/N: ")
            cont_loop = cont_loop.lower()
            if cont_loop == "y":
                cont_loop = True
            else:
                break
 
if __name__ == "__main__":
    main()