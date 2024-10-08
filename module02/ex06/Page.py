#!/usr/bin/python3

import elements as el
from elem import Elem, Text


class Page:
    def __init__(self, tree):
        if not self.__is_derived_from_elem(tree):
            raise Exception("Page argument is not derived from Elem")
        self.validate_tags_table = {
            "html": self.__is_html_ok,
            "head": self.__is_head_ok,
            "body": self.__is_body_and_div_ok,
            "div": self.__is_body_and_div_ok,
            "title": self.__is_containing_only_text,
            "h1": self.__is_containing_only_text,
            "h2": self.__is_containing_only_text,
            "li": self.__is_containing_only_text,
            "th": self.__is_containing_only_text,
            "td": self.__is_containing_only_text,
            "p": self.__is_containing_only_text,
            "span": self.__is_span_ok,
            "ul": self.__is_list_ok,
            "ol": self.__is_list_ok,
            "tr": self.__is_tr_ok,
            "table": self.__is_table_ok,
        }
        self.tree = tree

    def __str__(self):
        str = self.tree.__str__()
        if isinstance(self.tree, el.Html):
            str = "<!DOCTYPE html>\n" + str
        return str

    def write_to_file(self, filename):
        try:
            with open(filename, "w") as file:
                file.write(self.__str__())
        except Exception as e:
            print(e)
            exit(1)

    def is_valid(self):
        return self.__is_valid(self.tree)

    def __is_valid(self, content):
        if not self.__is_elem_or_text(content) and not isinstance(content, list):
            return False
        if isinstance(content, list):
            for item in content:
                if isinstance(item, Text) or item.tag in self.validate_tags_table:
                    continue
                return self.__is_valid(item.content)
        elif self.__is_derived_from_elem(content):
            if isinstance(content, Text):
                return True
            tag_exist = content.tag in self.validate_tags_table
            if tag_exist and not self.validate_tags_table[content.tag](content):
                return False
            return self.__is_valid(content.content)
        return True

    def __is_elem_or_text(self, to_check):
        return self.__is_derived_from_elem(to_check) or self.__is_text(to_check)

    def __is_derived_from_elem(self, to_check):
        return isinstance(to_check, Elem) and type(to_check) is not Elem

    def __is_text(self, to_check):
        return isinstance(to_check, Text)

    def __is_html_ok(self, html):
        """Html must strictly contain a Head, then a Body."""
        return (
            not isinstance(html, el.Html)
            or isinstance(html.content, list)
            and len(html.content) == 2
            and isinstance(html.content[0], el.Head)
            and isinstance(html.content[1], el.Body)
        )

    def __is_head_ok(self, head):
        """Head must only contain one Title and only one Title."""
        if isinstance(head.content, list):
            return len(head.content) == 1 and isinstance(head.content[0], el.Title)
        return isinstance(head.content, el.Title)

    def __is_body_and_div_ok(self, content):
        """Body and Div must only contain the following type of elements:
        H1, H2, Div, Table, Ul, Ol, Span, or Text."""
        valid_types = (el.H1, el.H2, el.Div, el.Table, el.Ul, el.Ol, el.Span, Text)
        if isinstance(content.content, list):
            return all([isinstance(item, valid_types) for item in content.content])
        return isinstance(content.content, valid_types)

    def __is_containing_only_text(self, content):
        """Title, H1, H2, Li, Th, Td
        must only contain one Text and only this Text"""
        if isinstance(content.content, list):
            return len(content.content) == 1 and isinstance(content.content[0], Text)
        return isinstance(content.content, Text)

    def __is_span_ok(self, span):
        """Span must only contain Text or some P."""
        if isinstance(span.content, list):
            return all([isinstance(item, (Text, el.P)) for item in span.content])
        return isinstance(span.content, (Text, el.P))

    def __is_list_ok(self, lst):
        """Ul and Ol must contain at least one Li and only some Li."""
        if isinstance(lst.content, list):
            if len(lst.content) == 0:
                return False
            return all([isinstance(item, el.Li) for item in lst.content])
        return isinstance(lst.content, el.Li)

    def __is_tr_ok(self, tr):
        """Tr must contain at least one Th or Td and only some Th or Td.
        The Th and the Td must be mutually exclusive."""
        if isinstance(tr.content, list):
            if len(tr.content) == 0:
                return False
            contain_only_th = all([isinstance(item, el.Th) for item in tr.content])
            contain_only_td = all([isinstance(item, el.Td) for item in tr.content])
            return contain_only_th or contain_only_td

        return isinstance(tr.content, (el.Th, el.Td))

    def __is_table_ok(self, table):
        """Table: must only contain Tr and only some Tr."""
        if isinstance(table.content, list):
            return all([isinstance(item, el.Tr) for item in table.content])
        return isinstance(table.content, el.Tr)


if __name__ == "__main__":
    table = el.Table(
        [
            el.Tr([el.Th(Text("Firstname")), el.Th(Text("Lastname"))]),
            el.Tr([el.Td(Text("John")), el.Td(Text("Doe"))]),
            el.Tr([el.Td(Text("Jane")), el.Td(Text("Doe"))]),
        ]
    )
    lst = el.Ul(
        [
            el.Li(Text("Flour")),
            el.Li(Text("Baking powder")),
            el.Li(Text("Suggar")),
            el.Li(Text("Salt")),
            el.Li(Text("Milk")),
            el.Li(Text("Butter")),
            el.Li(Text("Egg")),
        ]
    )

    head = el.Head(el.Title(Text("this is the title")))
    body = el.Body(
        [
            el.H1(Text("This is a table:")),
            el.Div(attr={"style": "border:1px solid grey"}, content=table),
            el.H2(Text("Pancake ingredients:")),
            lst,
        ]
    )
    page = Page(el.Html([head, body]))
    page.write_to_file("test.html")
    print(Page(el.P(Text("don't contain doctype"))))
