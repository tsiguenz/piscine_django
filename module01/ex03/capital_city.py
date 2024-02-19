#!/usr/bin/python3

import sys


def get_capital_from_state(states, capital_cities, state):
    short = states.get(state)
    print(capital_cities.get(short)) if short else print('Unknown state')


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
    get_capital_from_state(states, capital_cities, sys.argv[1])
