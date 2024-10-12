#!/usr/bin/python3

import sys

import requests
from bs4 import BeautifulSoup


def usage():
    print("Usage: python3 roads_to_philosophy.py <term>")


def get_next_term(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("It leads to a dead end !")
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find(id="mw-content-text")
    all_p = content.find_all("p")
    for p in all_p:
        links = p.find_all("a")
        for link in links:
            href = link.get("href")
            if "#" in href or "/Help:" in href:
                continue
            return href.split("/")[-1]
    raise Exception("It leads to a dead end !")


def main():
    if len(sys.argv) != 2:
        usage()
        exit(1)
    base_url = "https://en.wikipedia.org/wiki/"
    term = sys.argv[1].strip()
    terms = [term]
    while True:
        next_term = get_next_term(base_url + terms[-1])
        if next_term in terms:
            # for term in terms:
            #     print(term)
            raise Exception("It leads to an infinite loop !")
            exit(1)
        terms.append(next_term)
        if terms[-1] is None:
            exit(1)
        if terms[-1] == "Philosophy":
            break
    for term in terms:
        print(term)
    print(f"{len(terms)} roads from {term} to Philosophy")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        exit(1)
