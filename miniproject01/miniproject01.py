#!/usr/bin/env python3
"""This program will allow a user to select from a list of 3 states and generate a road trip itinerary from the selected state"""

def main():

    while True:
        states = {
            "CA": "California",
            "NV": "Nevada",
            "OR": "Oregon",
        }
        states_long = states.values()
        print("The states to choose from include", states["CA"], ",", states["NV"], ", and", states["OR"])
        sel_state = input("Please input which state you would like to travel to: ") 
        sel_state = sel_state.title()
        if sel_state == 'California':
            calif_itin = {
                "Itinerary 1" : "Los Angeles - Monterey - San Francisco",
                "Itinerary 2" : "San Diego - Mammoth - Lake Tahoe"
            }
            for k, v in calif_itin.items():
                print(k, v)
            break
        elif sel_state == 'Nevada':
            nev_itin = {
                "Itinerary 1" : "Las Vegas - Reno - Lake Tahoe",
                "Itinerary 2" : "Winnemuca - Reno - Las Vegas"
            }
            for k, v in nev_itin.items():
                print(k, v)
            break
        elif sel_state == 'Oregon':
            or_itin = {
                "Itinerary 1" : "Baker City - Portland - Medford",
                "Itinerary 2" : "Burns - Klamath Falls - Medford"
            }
            for k,v in or_itin.items():
                print(k, v)
            break
        else:
            print("Your input didn't match any of the above states, please input one of the three states.")
 
if __name__ == "__main__":
    main()