#!/usr/bin/python3

import sys

import requests
from bs4 import BeautifulSoup


def usage():
    print("Usage: python3 roads_to_philosophy.py <term>")


def get_title(soup):
    elem = soup.find("h1")
    return elem.text if elem else None


def is_valid_wikipedia_article_link(link):
    return (
        link is not None
        and (
            link.startswith("https://en.wikipedia.org/wiki/")
            or link.startswith("/wiki/")
        )
        and "#" not in link
        and "/Help:" not in link
        and "/File:" not in link
        and "/Category:" not in link
        and "/Talk:" not in link
        and "/Special:" not in link
        and "/Template:" not in link
        and "/Wikipedia:" not in link
    )


def is_parent_ok(a):
    if a.find_parent(role=["note", "presentation"]):
        return False
    if a.find_parent(class_=["side-box-text", "sidebar", "thumb"]):
        return False
    if a.find_parent(["table", "figure"]):
        return False
    return True


def get_first_link(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("It leads to a dead end !")
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find(id="mw-content-text")
    all_a = content.find_all("a")
    for a in all_a:
        href = a.get("href")
        if not is_valid_wikipedia_article_link(href) or not is_parent_ok(a):
            continue
        next_term = href.split("/")[-1]
        title = get_title(soup)
        if title in titles:
            # print(titles)
            raise Exception("It leads to an infinite loop !")
        titles.append(title)
        return next_term
    raise Exception("It leads to a dead end !")


def main():
    if len(sys.argv) != 2:
        usage()
        exit(1)
    base_url = "https://en.wikipedia.org/wiki/"
    base_term = sys.argv[1].strip()
    next_term = base_term
    while True:
        next_term = get_first_link(base_url + next_term)
        if titles[-1] == "Philosophy":
            break
    for base_term in titles:
        print(base_term)
    print(f"{len(titles)} roads from {base_term} to Philosophy")


if __name__ == "__main__":
    titles = []
    try:
        main()
    except Exception as e:
        print(e)
        exit(1)
