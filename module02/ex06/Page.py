#!/usr/bin/python3
import elements as el
from elem import Elem, Text


class Page:
    def __init__(self, tree):
        # check if all elements in tree are elem or text
        # if not self.__is_derived_from_elem(tree):
        #     raise Exception("Page agument is not a subclass of Elem")
        self.tree = tree

    def __str__(self):
        return self.tree.__str__()

    def is_valid(self):
        return self.__is_types_valid(self.tree) and self.__is_html_ok()

    def __is_types_valid(self, content):
        if not self.__is_elem_or_text(content) and not isinstance(content, list):
            return False
        if isinstance(content, list):
            for item in content:
                if not self.__is_types_valid(item):
                    return False
        elif self.__is_derived_from_elem(content):
            return self.__is_types_valid(content.content)
        return True

    def __is_elem_or_text(self, to_check):
        return self.__is_derived_from_elem(to_check) or self.__is_text(to_check)

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
    pass
