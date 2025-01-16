#!/usr/bin/python3

import sys

import requests
from bs4 import BeautifulSoup


def usage():
    print("Usage: python3 roads_to_philosophy.py <term>")


def get_title(soup):
    elem = soup.find("h1")
    return elem.text if elem else None


def get_next_term(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("It leads to a dead end !")
    soup = BeautifulSoup(response.text, "html.parser")
    title = get_title(soup)
    content = soup.find(id="mw-content-text")
    all_p = content.find_all("p")
    for p in all_p:
        links = p.find_all("a")
        for link in links:
            href = link.get("href")
            next_term = href.split("/")[-1]
            if (
                "/wiki/" not in href
                or "#" in href
                or "/Help:" in href
                or "/File:" in href
                or title is next_term
            ):
                continue
            return (title, next_term)
    raise Exception("It leads to a dead end !")


def main():
    if len(sys.argv) != 2:
        usage()
        exit(1)
    base_url = "https://en.wikipedia.org/wiki/"
    term = sys.argv[1].strip()
    titles = []
    next_term = term
    while True:
        actual_title, next_term = get_next_term(base_url + next_term)
        if actual_title is None:
            print("Error: actual_title is None")
            exit(1)
        if actual_title in titles:
            # for t in titles:
            #     print(t)
            raise Exception("It leads to an infinite loop !")
            exit(1)
        titles.append(actual_title)
        if actual_title == "Philosophy":
            break
    for term in titles:
        print(term)
    print(f"{len(titles)} roads from {term} to Philosophy")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        exit(1)
