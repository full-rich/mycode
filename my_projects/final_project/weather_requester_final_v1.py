#!/usr/bin/python3
"""application to provide weather forecast for user-inputted locations refactored"""

import requests
import csv
from pprint import pprint
from random import randint
from time import sleep

class Itinerary:
    
    def __init__(self):

        self.itin = []
        self.stop = []
        self.city = []
        self.state = []
        self.day = []
        self.loc_coord = []

    def input_itin(self):
             
        num_stops = int(input("Please input number of stops: "))
        stops_list = list(range(0,num_stops))
        city_list = []
        state_list = []
        day_list = []

        for stop in range(len(stops_list)):
            curr_stop = stop + 1
            city = str(input(f"Please enter the city for stop #{curr_stop} --> "))
            city = city.title()
            city_list.append(city)
                
            state = str(input(f"Please enter the state abbreviation for first stop #{curr_stop} --> "))
            state = state.upper()
            state_list.append(state)

            day = str(input(f"Please enter the day of the week you will stop #{curr_stop} --> "))
            day = day.title()
            day_list.append(day)
        
        with open("input_table.txt", "w") as input_table:
            input_table.write(f"{city_list}\n{state_list}\n{day_list}")

        self.stop = stops_list
        self.city = city_list
        self.state = state_list
        self.day = day_list

        return self

    def validate_itin(self):
        headers = {
            'User-Agent': 'dcb-weather-requester',
            'From': '{darrinbliler@gmail.com}'
        }

        while True: 
            url_list = []
            for city_index in range(len(self.city)):
                city_for_url = self.city[city_index]
                state_for_url = self.state[city_index]
                with open("bingapikey.txt", "r") as mykeyfile:
                    readmykeyfile = mykeyfile.read().rstrip('\n')
                    url_list.append(f"http://dev.virtualearth.net/REST/v1/Locations?CountryRegion=&adminDistrict={state_for_url}&locality={city_for_url}&key={readmykeyfile}")

            loc_res_list = []
            loc_res_admin_dist = []
            loc_res_country = []
            loc_res_admin_dist_list = []
            loc_res_country_list = []

            for url_index in range(len(url_list)):
                url = url_list[url_index]
                loc_res = requests.get(url, headers=headers).json()
                sleep(randint(3,7))
                loc_res_list.append(loc_res)            
                
                loc_res_admin_dist = loc_res['resourceSets'][0]['resources'][0]['address']['adminDistrict']
                loc_res_country = loc_res['resourceSets'][0]['resources'][0]['address']['countryRegion']
                
                loc_res_admin_dist_list.append(loc_res_admin_dist)
                loc_res_country_list.append(loc_res_country)
            
            for admin_dist in range(len(loc_res_admin_dist_list)):
                count = admin_dist + 1
                print(f"The location you entered matched our geographical database for stop #{count} in {loc_res_admin_dist_list[admin_dist]}, {loc_res_country_list[admin_dist]}.")
            
            print("Do these look correct?")
            print("1. Yes")
            print("2. No")
            option = int(input("> (1/2): "))

            # create list to hold latitude and longitude for each stop
            loc_coord = []
            if option == 1:
                for index in range(len(loc_res_list)):
                    loc_coord.append(loc_res_list[index]['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates'])
                
                coord_num = len(loc_coord)
                index = 0
                while index < coord_num:
                    loc_coord[index][0] = round(loc_coord[index][0], 4)
                    loc_coord[index][1] = round(loc_coord[index][1], 4)
                    index += 1
                    
                with open("nws_coord.txt", "w", newline='') as nws_coord:
                    index = 0
                    coord_num = len(loc_coord)
                    while index < coord_num:
                        count = index + 1
                        if count == coord_num:
                            nws_coord.write(f"{loc_coord[index][0]},{loc_coord[index][1]}")
                        else:
                            nws_coord.write(f"{loc_coord[index][0]},{loc_coord[index][1]}\n")
                        index += 1

                break

            elif option == 2:
                print("Please re-run the app to make a new itinerary.")
                break
            
            else:
                return self

def get_grids():
    """get NWS grid urls"""

    with open("nws_coord.txt", "r") as nws_coord:
        nws_coord_list = nws_coord.readlines()
        url_root = "https://api.weather.gov/points/"
        
        
        with open("nws_grid_urls.txt", "w") as nws_grid_urls:
            index = 0
            coord_num = len(nws_coord_list)
            while index < coord_num:
                nws_grid_urls.write(f"{url_root}{nws_coord_list[index]}")
                index += 1
    
def get_fc_urls():
    """get forecast urls"""

    headers = {
            'User-Agent': 'dcb-weather-requester',
            'From': '{darrinbliler@gmail.com}'
        }    

    with open("nws_grid_urls.txt", "r") as nws_grid_urls:

        # place urls into a list
        nws_url_list = nws_grid_urls.readlines()
        nws_urls = [url.rstrip('\n') for url in nws_url_list]

        # create a list for the response
        nws_response = []

        # request urls for forecast based on grid
        for item in range(len(nws_urls)):
            response = nws_urls[item]
            nws_request = requests.get(response, headers=headers).json()
            sleep(randint(3,7))
            nws_response.append(nws_request)
        
        # create a new list to hold the first dictionary extract
        response_slice = []

        # extract properties section from request dictionary (grid url lives a couple levels deep)
        for item in range(len(nws_response)):
            properties = nws_response[item].get('properties')
            sleep(randint(3,7))
            response_slice.append(properties)

        # create a new list to hold the url itself
        fc_urls = []

        # extract forecast urls and place in list
        for item in range(len(response_slice)):
            links = response_slice[item].get('forecast')
            fc_urls.append(links)

    # write forecast urls to .txt
    with open("nws_fc_urls.txt", "w") as nws_fc_urls:
        index = 0
        grid_url = len(fc_urls)
        while index < grid_url:
            nws_fc_urls.write(f"{fc_urls[index]}\n")
            index += 1

def get_fc():
    """get forecast from nws based on grid links"""
    
    headers = {
            'User-Agent': 'dcb-weather-requester',
            'From': '{darrinbliler@gmail.com}'
        }    

    with open("nws_fc_urls.txt", "r") as nws_fc_urls:

        # place urls into a list
        nws_url_list = nws_fc_urls.readlines()

        nws_urls = [url.rstrip('\n') for url in nws_url_list]


    # create a list for the response
    nws_response = []

    # request forecast
    for item in range(len(nws_urls)):
        response = nws_urls[item]
        nws_request = requests.get(response, headers=headers).json()
        sleep(randint(3,7))
        nws_response.append(nws_request)
    
    # create a new list to hold the first parsed dictionary extract
    response_slice = []

    # extract properties section to retrieve forecast
    for item in range(len(nws_response)):
        properties = nws_response[item].get('properties')
        response_slice.append(properties)      

    # create a new list to hold the forecast itself
    fc = []

    # extract forecast urls and place in list. 'periods' holds forecast dictionary.
    for item in range(len(response_slice)):
        periods = response_slice[item].get('periods')
        fc.append(periods)

    pprint(fc)


def main():

    itinerary1 = Itinerary()

    itinerary1.input_itin()

    itinerary1.validate_itin()       

    get_grids()

    get_fc_urls()

    get_fc()
    

if __name__ == '__main__':
    main()