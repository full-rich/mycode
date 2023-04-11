#!/usr/bin/env python3

def main():
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)")
    char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)")
    char_name = char_name.title()
    char_stat = char_stat.lower()
    marvelchars= {
    "Starlord": {
        "real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
        },

    "Mystique": {
        "real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"
        },

    "Hulk":
        {"real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"}
        }
    
    stat = marvelchars[char_name][char_stat]
    print(f"{char_name} is {stat}")

    print(marvelchars.get(char_name))


    #print(type(char_name))
    #print(type(char_stat))
    #print(char_name)
    #print(char_stat)
    #char_out = marvelchars.get(char_name)
    #char_out2 = char_name.get(char_stat)
    
    #print(char_out)
    #print(char_out2)
    #print(f"{char_name}'s {char_stat} is: {char_out2}")

if __name__ == "__main__":
    main()