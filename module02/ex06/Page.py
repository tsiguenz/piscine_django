#!/usr/bin/python3
import elements as el
from elem import Elem, Text


class Page:
    def __init__(self, tree):
        # check if all elements in tree are elem or text
        if not self.__is_derived_from_elem(tree):
            raise Exception("Page agument is not a subclass of Elem")
        self.tree = tree

    def __str__(self):
        return self.tree.__str__()

    def is_valid(self):
        if self.__is_html_ok() is False:
            return False
        return True

    def __is_derived_from_elem(self, to_check):
        return isinstance(to_check, Elem) and type(to_check) is not Elem

    def __is_text(self, to_check):
        return isinstance(to_check, Text)

    def __is_html_ok(self):
        # should html be the first element ?
        return (
            not isinstance(self.tree, el.Html)
            or isinstance(self.tree.content, list)
            and len(self.tree.content) == 2
            and isinstance(self.tree.content[0], el.Head)
            and isinstance(self.tree.content[1], el.Body)
        )


if __name__ == "__main__":
    # Html must strictly contain a Head, then a Body
    assert Page(el.Html()).is_valid() is False
    assert Page(el.Html(el.Body())).is_valid() is False
    assert Page(el.Html([el.Body(), el.Head()])).is_valid() is False
    assert Page(el.Html([el.H1(), el.Body()])).is_valid() is False
    assert Page(el.Html([el.Head(), el.H1()])).is_valid() is False
    assert Page(el.Html([el.Head(), el.Body()])).is_valid() is True
