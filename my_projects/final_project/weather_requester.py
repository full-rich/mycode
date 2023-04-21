#!/usr/bin/python3
"""application to provide weather forecast for user-inputted locations"""

# import tools
from geopy.geocoders import Nominatim
import requests
from pprint import pprint

def get_lat_lon(city_input, state_input):

    ## mykey is our Bing maps key
    with open("bingapikey.txt", "r") as mykeyfile:
        readmykeyfile = mykeyfile.read()
        URL_loc = f"http://dev.virtualearth.net/REST/v1/Locations?CountryRegion=&adminDistrict={state_input}&locality={city_input}&key={readmykeyfile}"
    
    loc_req = requests.get(URL_loc).json()
    pprint(loc_req)

    # add error handling if no result

    loc_country = loc_req['resourceSets'][0]['resources'][0]['address']['countryRegion']
    if loc_country != 'United States':
        print("It looks like you input a city outside the United States. Sorry, the app only gets weather for cities in the United States. We hope to expand soon!")
    else:
        loc_coord = loc_req['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates']   # get point coordinates for the city, state input
    
    loc_lat_trunc = round(loc_coord[0], 4)    # truncate to 4 digits to comply with NWS weather API {latitude},{longitude} limits
    loc_lon_trunc = round(loc_coord[1], 4)    # truncate to 4 digits to comply with NWS weather API {latitude},{longitude} limits
    get_nws_fc(loc_lat_trunc, loc_lon_trunc)

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

        # iterate through each period
        for period in range(len(nws_return_fc_output)):
            nws_return_fc.write(f"{nws_return_fc_output[period]['name']}: {nws_return_fc_output[period]['detailedForecast']} '\n'")
    

def main():
    city_input = input("Please input a city: ")    # get user-requested city

    city_input = city_input.title()    # format to capitalize first letter of city - if multiple words, capitalizes first letter of each word in city name
    
    state_input = input("Please input a state: ")    # get user-requested state

    state_input = state_input.upper()    # place state into upper case

    print(f"You input {city_input}, {state_input} '\n'")    # print out the inputted city, state

    get_lat_lon(city_input, state_input)

    print(f"Weather forecast for {city_input}, {state_input}'\n'")

    with open("nws_return_fc_output.txt", "r") as forecast:
        for line in forecast:
            print(line + '\n')

if __name__ == '__main__':
    main()


    #def get_lat_long(user_input):
        #user input = input()
    #def main():
       # lat_long = get_lat_long(argument):
