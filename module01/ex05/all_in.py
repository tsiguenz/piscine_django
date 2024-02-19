#!/usr/bin/python3

import sys


def init_capitals_and_states():
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
    return capital_cities, states


def get_state_from_capital(capital, states, capital_cities):
    shortState = None
    for key, value in capital_cities.items():
        if value.lower() == capital.lower():
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
        if key.lower() == state.lower():
            state = key
            shortState = value
            return capital_cities.get(shortState), state
    return None, None


def print_capital_or_state_from_argv():
    if len(sys.argv) != 2:
        exit(0)
    argv = sys.argv[1]
    if ',,' in argv:
        exit(0)
    args = argv.split(',')
    args = [arg.strip() for arg in args]
    args = [" ".join(arg.split()) for arg in args]
    capital_cities, states = init_capitals_and_states()
    for arg in args:
        if not arg:
            continue
        state, capital = get_state_from_capital(arg, states, capital_cities)
        if state and capital:
            print(f"{capital} is the capital of {state}")
            continue
        capital, state = get_capital_from_state(arg, states, capital_cities)
        if capital and state:
            print(f"{capital} is the capital of {state}")
            continue
        print(arg, "is neither a capital city nor a state")


if __name__ == '__main__':
    print_capital_or_state_from_argv()
