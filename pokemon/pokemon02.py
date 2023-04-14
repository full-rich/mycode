#!/usr/bin/env python3

import requests



def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    #print(pokeapi)
    # pokeapi["sprites"]["front_default"] # part 1 challenge
    char_game_count = 0
    for x in pokeapi["game_indices"]:
        pokeapi["game_indices"]
        char_game_count += 1
    print(char_game_count)

main()