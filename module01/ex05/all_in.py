#!/usr/bin/python3

import sys


def get_state_from_capital(capital, states, capital_cities):
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
    shortState = None
    for key, value in capital_cities.items():
        if value.lower() == capital:
            capital = value
            shortState = key
            break
    for key, value in states.items():
        if value == shortState:
            return key, capital
    return None, None


def get_capital_from_state(state, states, capital_cities):
    shortState = None
    for key, value in states.items():
        if key.lower() == state:
            state = key
            shortState = value
            return capital_cities.get(shortState), state
    return None, None


def print_capital_or_state_from_argv():
    if len(sys.argv) != 2:
        exit(0)
    argv = sys.argv[1]
    argv = argv.lower()
    argv = argv.replace(' ', '')
    if argv.find(',,') != -1:
        exit(0)
    args = argv.split(',')
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
    for arg in args:
        state, capital = get_state_from_capital(arg, states, capital_cities)
        if state and capital:
            print(f"{capital} is the capital of {state}")
            continue
        capital, state = get_capital_from_state(arg, states, capital_cities)
        if capital and state:
            print(f"The capital of {state} is {capital}")
            continue
        print(arg, "is neither a capital city nor a state")


if __name__ == '__main__':
    print_capital_or_state_from_argv()
