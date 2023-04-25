#!/usr/bin/python3
"""application to provide weather forecast for user-inputted locations"""

# import tools
import requests
from pprint import pprint

def get_lat_lon(city_input, state_input):
    """provides latitude and longitude for location"""
    
    ## mykey is our Bing maps key
    with open("bingapikey.txt", "r") as mykeyfile:
        readmykeyfile = mykeyfile.read()
        URL_loc = f"http://dev.virtualearth.net/REST/v1/Locations?CountryRegion=&adminDistrict={state_input}&locality={city_input}&key={readmykeyfile}"
    
    loc_req = requests.get(URL_loc).json()
    #pprint(loc_req)

    # add error handling if no result

    loc_country = loc_req['resourceSets'][0]['resources'][0]['address']['countryRegion']
    
    try:
        if loc_country == 'United States':
            
            loc_coord = loc_req['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates']   # get point coordinates for the city, state input
            loc_lat_trunc = round(loc_coord[0], 4)    # truncate to 4 digits to comply with NWS weather API {latitude},{longitude} limits
            loc_lon_trunc = round(loc_coord[1], 4)    # truncate to 4 digits to comply with NWS weather API {latitude},{longitude} limits
            get_nws_fc(loc_lat_trunc, loc_lon_trunc)
        
        else:
            print("It looks like you input a city outside the United States. Sorry, the app only gets weather for cities in the United States. We hope to expand soon!")            
    except:
        x = 'General error with getting coordinates.'
    else:
        x = 'No error.'
    # if error is received while generating coordinates, log it
    finally:
        with open("loc_coord_error_log.txt", "w") as zlog:
            print(x, file = zlog)

    

def get_nws_fc(loc_lat_trunc, loc_lon_trunc):

    URL = "https://api.weather.gov/points/"
    nws_api = requests.get(f"{URL}{loc_lat_trunc},{loc_lon_trunc}").json()    # request grid endpoint from "forecast" property
    
    # pprint(nws_api)
    nws_forecast_url_properties = nws_api.get('properties')    # parse properties to get to forecast url
    nws_forecast_url = nws_forecast_url_properties.get('forecast')    # extract forecast url
    #print(nws_forecast_url)

    # request result from forecast url
    nws_return_forecast = requests.get(nws_forecast_url).json()
    #pprint(nws_return_forecast)

    # extract relevant forecast dict
    nws_return_fc_output = nws_return_forecast['properties']['periods']
    
    with open("nws_return_fc_output.txt", "w") as nws_return_fc:
        
        # print which NWS city and NWS state were forecasted to provide transparency to the user
        print(f"NWS forecast city: ")
        # iterate through each period
        for period in range(len(nws_return_fc_output)):
            nws_return_fc.write(f"{nws_return_fc_output[period]['name']}: {nws_return_fc_output[period]['detailedForecast']} '\n'")
    

def main():
    
    """trip_dict = {
            'trip nights'     : 0,
            'modify trip'     : True,
            'overnight stops' : {
                                    1 : {
                                            'city'   : '',
                                            'state'  : '',
                                            'lat'    : 0.0000,
                                            'lon'    : 0.0000,
                                            'day'    : {
                                                            1 : {
                                                                'day forecast'   : '',
                                                                'night forecast' : ''
                                                            }
                                            }
                                    }
            }
        }

    try:
        vac_nights = int(input("How many nights will you be on your road trip (1-5 days)? --> "))

    except ValueError as verr:
                        print("Please enter a value between 1-5.")
    
    else:
                        min_trip_duration = 1
                        max_trip_duration = 5
                        if trip_nights > max_trip_duration or trip_nights < min_trip_duration:
                            print("Please enter a value between 1-5")
                        else:
                            break
    
    trip_dict['trip nights'] == vac_nights"""



    while True:

        print("\nWelcome to ROAD TRIP WEATHER (US) App\n")
        print("This app will provide a weather forecast for your road trip within the 50 United States. Duration is limited to 5 days/nights.")
        print("Weather data provided by U.S. National Weather Service.\n")

        #initialize loop for running app
        while True:
            
            # initialize loop for handling user input for trip duration
            while True:
                
                while True:
                    try:
                        trip_nights = int(input("How many nights will you be on your road trip (1-5 days)? --> "))
                        
                    except ValueError as verr:
                        print("Please enter a value between 1-5.")

                    else:
                        min_trip_duration = 1
                        max_trip_duration = 5
                        if trip_nights > max_trip_duration or trip_nights < min_trip_duration:
                            print("Please enter a value between 1-5")
                        else:
                            break
            
                city_input = input("Please input a city: ")    # get user-requested city

                city_input = city_input.title()    # format to capitalize first letter of city - if multiple words, capitalizes first letter of each word in city name
            
                states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Washington DC', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
                state_input = input("Please input a state: ")    # get user-requested state
                state_input = state_input.upper()    # place state into upper case

                if state_input in states:

                    get_lat_lon(city_input, state_input)

                    print(f"Weather forecast for {city_input}, {state_input}'\n'")
                
                    with open("nws_return_fc_output.txt", "r") as forecast:
                        for line in forecast:
                            print(line + '\n')
                    break
                
                else:
                    print("It looks like you didn't input one of the 50 states. Please enter one of the 50 states abbreviated or spelled out.")
            break

        while True:
            print("Would you like to generate a weather report for another trip?")
            loop_var = str(input("Yes or No? --> ")).lower()
            loop_var_ok = ('y', 'no', 'yes', 'n')

            if loop_var == 'no' or loop_var == 'n':
                new_report = False
                break
            elif loop_var not in loop_var_ok:
                print("That's not a valid response. Please enter yes, no, y, or n.")
            else:
                new_report = True
                break
        
        if new_report == True:
            True
        else:
            break
        


            
if __name__ == '__main__':
    main()


    #def get_lat_long(user_input):
        #user input = input()
    #def main():
       # lat_long = get_lat_long(argument):
