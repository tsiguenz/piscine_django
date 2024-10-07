#!/usr/bin/python3

import traceback
import elements as el
from elem import Text
from Page import Page


def types_of_every_item_in_tree():
    """If, on the tree path, a node has not one of the following types:
    html, head, body, title, meta, img, table, th, tr, td , ul, ol, li, h1,
    h2, p, div, span, hr, br or Text, the tree is invalid"""
    # assert Page(el.P()).is_valid() is True
    # assert Page(el.P(Text())).is_valid() is True
    # assert (
    #     Page(
    #         el.Html([el.Head(el.Title(Text())), el.Body([el.P(Text()), el.P(Text())])])
    #     ).is_valid()
    #     is True
    # )
    # assert Page(el.P("not valid")).is_valid() is False
    assert (
        Page(el.Html([el.Head(el.Title(Text())), el.Body([el.P(), el.P()])])).is_valid()
        is False
    )


def head_and_body_in_html():
    """Html must strictly contain a Head, then a Body"""
    assert Page(el.Html()).is_valid() is False
    assert Page(el.Html(el.Body())).is_valid() is False
    assert Page(el.Html([el.Body(), el.Head()])).is_valid() is False
    assert Page(el.Html([el.H1(), el.Body()])).is_valid() is False
    assert Page(el.Html([el.Head(), el.H1()])).is_valid() is False
    assert Page(el.Html([el.Head(), el.Body()])).is_valid() is True


def test():
    # head_and_body_in_html()
    types_of_every_item_in_tree()


if __name__ == "__main__":
    GREEN = "\033[92m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    try:
        test()
        print(GREEN + "Tests success" + ENDC)
    except AssertionError as e:
        traceback.print_exc()
        print(e)
        print(RED + "Tests failed" + ENDC)
