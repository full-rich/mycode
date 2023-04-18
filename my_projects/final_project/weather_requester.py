#!/usr/bin/python3
"""application to provide weather forecast for user-inputted locations"""

# import tools
from geopy.geocoders import Nominatim
import requests
from pprint import pprint

#def city_state():

def main():

    city_input = input("Please input a city: ")    # get user-requested city

    city_input_title = city_input.title()    # format to capitalize first letter of city - if multiple words, capitalizes first letter of each word in city name
    
    state_input = input("Please input a state: ")    # get user-requested state

    state_input_upper = state_input.upper()    # place state into upper case

    print(f"You input {city_input_title}, {state_input_upper}")    # print out the inputted city, state

    city_state_dict = {'city' : city_input_title, 'state' : state_input_upper}    # store the city state as a key, value pair in python dictionary format

    location_request = Nominatim(user_agent="dcb-weatherrequester")    # comply with Nominatim Usage Policy by specifiying custom user_agent

    location = location_request.geocode(city_state_dict, exactly_one=True) # request location data generation for city, state dictioary
    
    location_lat = location.latitude # retrieve location latitude
    
    location_lon = location.longitude    # retrieve location longitude

    location_lat_trunc = round(location_lat, 4)    # truncate to 4 digits to comply with NWS weather API {latitude},{longitude} limits
    location_lon_trunc = round(location_lon, 4)    # truncate to 4 digits to comply with NWS weather API {latitude},{longitude} limits
    
    URL = "https://api.weather.gov/points/"
    nws_api = requests.get(f"{URL}{location_lat_trunc},{location_lon_trunc}").json()    # request grid endpoint from "forecast" property
    # pprint(nws_api)
    nws_forecast_url_properties = nws_api.get('properties')    # parse properties to get to forecast url
    nws_forecast_url = nws_forecast_url_properties.get('forecast')    # extract forecast url
    print(nws_forecast_url)

if __name__ == '__main__':
    main()