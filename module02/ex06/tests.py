#!/usr/bin/python3

import traceback
import elements as el
from elem import Text
from Page import Page


def types_of_every_item_in_tree():
    """If, on the tree path, a node has not one of the following types:
    html, head, body, title, meta, img, table, th, tr, td , ul, ol, li, h1,
    h2, p, div, span, hr, br or Text, the tree is invalid"""
    assert Page(el.P(Text())).is_valid() is True
    assert Page(el.P(Text())).is_valid() is True
    assert (
        Page(
            el.Html([el.Head(el.Title(Text())), el.Body(
                [el.P(Text()), el.P(Text())])])
        ).is_valid()
        is True
    )
    res = True
    try:
        assert Page(42).is_valid() is False
        res = False
    except Exception:
        res = True
    assert res is True


def head_and_body_in_html():
    """Html must strictly contain a Head, then a Body"""
    assert Page(el.Html()).is_valid() is False
    assert Page(el.Html(el.Body())).is_valid() is False
    assert Page(el.Html([el.Body(), el.Head()])).is_valid() is False
    assert Page(el.Html([el.H1(), el.Body()])).is_valid() is False
    assert Page(el.Html([el.Head(), el.H1()])).is_valid() is False
    assert Page(el.Html([el.Head(), el.Body()])).is_valid() is True


def head_contain_only_title():
    """Head must only contain one Title and only one Title."""
    assert Page(el.Head(el.H1(Text()))).is_valid() is False
    assert Page(el.Head(el.Meta())).is_valid() is False
    assert Page(el.Head()).is_valid() is False
    assert (
        Page(el.Head([el.Title(Text("title")),
             el.Title(Text("title"))])).is_valid()
        is False
    )
    assert Page(el.Head(el.Title(Text("title")))).is_valid() is True


def check_body_and_div():
    """Body and Div must only contain the following type of elements:
    H1, H2, Div, Table, Ul, Ol, Span, or Text."""
    assert Page(el.Body([el.Table(), el.Span()])).is_valid() is True
    assert Page(el.Div([el.Text(), el.H1()])).is_valid() is True
    assert Page(el.Div([el.Text(), el.Body()])).is_valid() is False
    assert Page(el.Div([el.Text(), el.Body()])).is_valid() is False
    assert Page(el.Div(el.Body())).is_valid() is False


def check_elem_containing_only_text():
    """Title, H1, H2, Li, Th, Td
    must only contain one Text and only this Text"""
    assert Page(el.Title(Text("test"))).is_valid() is True
    assert Page(el.Title(el.P(Text("test")))).is_valid() is False


def test():
    head_and_body_in_html()
    types_of_every_item_in_tree()
    head_contain_only_title()
    check_body_and_div()
    check_elem_containing_only_text()


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
