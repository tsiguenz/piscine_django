#!/usr/bin/python3

import requests
import dewiki
import sys


def usage():
    print("Usage: python3 request_wikipedia.py <term>")


def write_to_file(filename, content):
    print(f'Writing content in {filename}')
    try:
        with open(filename, "w") as f:
            f.write(content)
    except Exception as e:
        print("Can't write to file:", e)

def get_wiki_content(term):
    print('Get wikipedia page from API')
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "parse",
        "page": term,
        "prop": "wikitext",
        "redirects": "true",
        "format": "json",
    }
    r = requests.get(url=URL, params=PARAMS)
    if r.status_code != 200:
        print('Bad status code')
        exit(1)
    json = r.json()
    if 'error' in json.keys():
        print('Error:', json['error']['info'])
        exit(1)
    return json["parse"]["wikitext"]["*"]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        usage()
        exit(1)
    term = sys.argv[1].strip().lower()
    filename = term.replace(" ", "_") + ".wiki"
    wikitext = get_wiki_content(term)
    write_to_file(filename, dewiki.from_string(wikitext))
