#!/usr/bin/python3

import requests
import json
import dewiki
import sys

def usage():
    print("Usage: python3 request_wikipedia.py <term>")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        usage()
    # https://en.wikipedia.org/w/api.php?action=parse&page=Pet_door&format=json 
    term = sys.argv[1].strip()
    wikipedia_api_url = f'https://en.wikipedia.org/w/api.php?action=parse&page={term}&format=json'
    file_name = term.replace(' ', '_') + '.wiki'
    r = requests.get(wikipedia_api_url)
    print(r.json()['parse']['text']['*'])
#    print(file_name)
#    print(wikipedia_api_url)
