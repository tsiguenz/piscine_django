#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.
    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        s = super()
        s = s.replace("<", "&lt;")
        s = s.replace(">", "&gt;")
        s = s.replace('"', "&quot;")
        s = s.replace("\n", "\n<br />\n")
        return s


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    class ValidationError(Exception):
        pass

    def __init__(self, tag="div", attr={}, content=None, tag_type="double"):
        """
        __init__() method.
        Obviously.
        """
        self.tag = tag
        self.attr = attr
        if content is None:
            content = []
        if not self.check_type(content):
            raise Elem.ValidationError
        self.content = content if type(content) is list else [content]
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything(tag, attributes, embedded
        elements...).
        """
        result = ""
        if self.tag_type == "double":
            result += f"<{self.tag}{self.__make_attr()}>"
            result += f"{self.__make_content()}"
            result += f"</{self.tag}>"
        elif self.tag_type == "simple":
            result = f"<{self.tag}{self.__make_attr()}/>"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ""
        for pair in sorted(self.attr.items()):
            result += " " + str(pair[0]) + '="' + str(pair[1]) + '" '
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if len(self.content) == 0:
            return ""
        result = "\n"
        for elem in self.content:
            if len(elem.__str__()) == 0:
                continue
            splitted_elem = elem.__str__().split("\n")
            for line in splitted_elem:
                result += f"  {line}\n"
        if result == "\n":
            return ""
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) is list:
            self.content += [elem for elem in content if elem != Text("")]
        elif content != Text(""):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (
            isinstance(content, Elem)
            or type(content) is Text
            or (
                type(content) is list
                and all(
                    [type(elem) is Text or isinstance(elem, Elem) for elem in content]
                )
            )
        )


if __name__ == "__main__":
    title = Elem(tag="title", content=Text('"Hello ground!"'))
    head = Elem(tag="head", content=title)
    h1 = Elem(tag="h1", content=Text('"Oh no, not again!"'))
    img = Elem(
        tag="img", attr={"src": "http://i.imgur.com/pfp3T.jpg"}, tag_type="simple"
    )
    body = Elem(tag="body", content=[h1, img])
    html = Elem(tag="html", content=[head, body])
    print(html)
    print(Elem(content=[42]))
