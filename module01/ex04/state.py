#!/usr/bin/python3

import sys


def get_state_from_capital(states, capital_cities, capital):
    shortState = None
    for key, value in capital_cities.items():
        if value == capital:
            shortState = key
            break
    for key, value in states.items():
        if value == shortState:
            print(key)
            return
    print("Unknown capital city")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(0)
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    get_state_from_capital(states, capital_cities, sys.argv[1])
