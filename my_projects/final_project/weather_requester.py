#!/usr/bin/python3
"""application to provide weather forecast for user-inputted locations"""

# import tools
from geopy.geocoders import Nominatim
import requests
from pprint import pprint

#def city_state():

def main():

    # get user-requested city
    city_input = input("Please input a city: ")

    # format to capitalize first letter of city - if multiple words, capitalizes first letter of each word in city name
    city_input_title = city_input.title()
    
    # get user-requested state
    state_input = input("Please input a state: ")

    # place state into upper case
    state_input_upper = state_input.upper()

    # print out the inputted city, state
    print(f"You input {city_input_title}, {state_input_upper}")

    # store the city state as a key, value pair in python dictionary format
    city_state_dict = {'city' : city_input_title, 'state' : state_input_upper}
    

#def geolocator(city, state):
    # comply with Nominatim Usage Policy by specifiying custom user_agent
    location_request = Nominatim(user_agent="dcb-weatherrequester")

    # request location data generation for city, state dictioary
    location = location_request.geocode(city_state_dict, exactly_one=True)
    
    # retrieve location latitude
    location_lat = location.latitude
    
    # retrieve location longitude
    location_lon = location.longitude

    # truncate to 4 digits to comply with NWS weather API {latitude},{longitude} limits
    location_lat_trunc = round(location_lat, 4)
    location_lon_trunc = round(location_lon, 4)
    
    URL = "https://api.weather.gov/points/"
    nws_api = requests.get(f"{URL}{location_lat_trunc},{location_lon_trunc}").json() # request grid endpoint from "forecast" property
    #pprint(nws_api)
    nws_forecast_url_properties = nws_api.get('properties')
    nws_forecast_url = nws_forecast_url_properties.get('forecast')
    # print(nws_forecast_url)

if __name__ == '__main__':
    main()

#if __name__ == '__weather_requester__':
    #city_state()
    #geolocator()