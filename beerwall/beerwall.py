#!/usr/bin/python3

def main():
    beer_start = "bottles of beer on the wall!"
    beer_interim = "bottles of beer!"
    beer_fin = "You take one down, pass it around!"
    bottles_rem = 99
    for bottles_rem in range(99):
        while bottles_rem != 0:
            print(f"{bottles_rem} {beer_start}/n {bottles_rem} {beer_start} {bottles_rem} {beer_fin}\n")
            bottles_rem = bottles_rem - 1

if __name__ == "__main__":
    main()