#!/usr/bin/python3

import sys


def get_capital_from_state(state):
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
    short = states.get(state)
    print(capital_cities.get(short)) if short else print('Unknow state')


if __name__ == '__main__':
    get_capital_from_state(sys.argv[1])
