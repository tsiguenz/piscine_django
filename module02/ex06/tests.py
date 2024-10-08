#!/usr/bin/python3

import traceback
import elements as el
from elem import Text
from Page import Page


def check_types():
    """If, on the tree path, a node has not one of the following types:
    html, head, body, title, meta, img, table, th, tr, td , ul, ol, li, h1,
    h2, p, div, span, hr, br or Text, the tree is invalid"""
    assert Page(el.P(Text())).is_valid() is True
    assert Page(el.P(Text())).is_valid() is True
    assert (
        Page(
            el.Html([el.Head(el.Title(Text())), el.Body([el.P(Text()), el.P(Text())])])
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


def check_head_and_body():
    """Html must strictly contain a Head, then a Body"""
    assert Page(el.Html()).is_valid() is False
    assert Page(el.Html(el.Body())).is_valid() is False
    assert Page(el.Html([el.Body(), el.Head()])).is_valid() is False
    assert Page(el.Html([el.H1(), el.Body()])).is_valid() is False
    assert Page(el.Html([el.Head(), el.H1()])).is_valid() is False
    assert Page(el.Html([el.Head(), el.Body()])).is_valid() is True


def check_head():
    """Head must only contain one Title and only one Title."""
    assert Page(el.Head(el.H1(Text()))).is_valid() is False
    assert Page(el.Head(el.Meta())).is_valid() is False
    assert Page(el.Head()).is_valid() is False
    assert (
        Page(el.Head([el.Title(Text("title")), el.Title(Text("title"))])).is_valid()
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


def check_span():
    """Span must only contain Text or some P."""
    assert Page(el.Span(Text("test"))).is_valid() is True
    assert Page(el.Span(el.P())).is_valid() is True
    assert Page(el.Span([el.P(), el.P()])).is_valid() is True
    assert Page(el.Span([el.P(), Text()])).is_valid() is True
    assert Page(el.Span(el.H1(Text()))).is_valid() is False
    assert Page(el.Span([el.P(), el.H1(Text())])).is_valid() is False


def check_list():
    """Ul and Ol must contain at least one Li and only some Li."""
    assert Page(el.Ul()).is_valid() is False
    assert Page(el.Ol()).is_valid() is False
    assert Page(el.Ul(el.P())).is_valid() is False
    assert Page(el.Ol(el.P())).is_valid() is False
    assert Page(el.Ul([el.Li(), el.P()])).is_valid() is False
    assert Page(el.Ol([el.Li(), el.P()])).is_valid() is False
    assert Page(el.Ul([el.Li(), el.Li()])).is_valid() is True
    assert Page(el.Ol([el.Li(), el.Li()])).is_valid() is True
    assert Page(el.Ul(el.Li())).is_valid() is True
    assert Page(el.Ol(el.Li())).is_valid() is True


def check_tr():
    """Tr must contain at least one Th or Td and only some Th or Td.
    The Th and the Td must be mutually exclusive."""
    assert Page(el.Tr()).is_valid() is False
    assert Page(el.Tr(el.P())).is_valid() is False
    assert Page(el.Tr(el.P())).is_valid() is False
    assert Page(el.Tr([el.Td(), el.Th()])).is_valid() is False
    assert Page(el.Tr([el.Th(), el.Td()])).is_valid() is False
    assert Page(el.Tr([el.Td(), el.Td()])).is_valid() is True
    assert Page(el.Tr([el.Th(), el.Th()])).is_valid() is True
    assert Page(el.Tr(el.Td())).is_valid() is True
    assert Page(el.Tr(el.Th())).is_valid() is True


def check_table():
    """Table: must only contain Tr and only some Tr."""
    assert Page(el.Table(Text())).is_valid() is False
    assert Page(el.Table([el.Tr(), el.P()])).is_valid() is False
    assert Page(el.Table(el.Tr())).is_valid() is True
    assert Page(el.Table()).is_valid() is True


def test():
    check_head_and_body()
    check_types()
    check_head()
    check_body_and_div()
    check_elem_containing_only_text()
    check_span()
    check_list()
    check_tr()
    check_table()


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
