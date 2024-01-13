#!/usr/bin/python3

def print_line(var):
    print(var, "has a type", type(var))


def my_var():
    integer = 42
    string1 = "42"
    string2 = "quarante-deux has a type"
    floatingNumber = 42.0
    boolean = True
    lst = [42]
    dictionary = {42: 42}
    tupl = (42,)
    emptySet = set()

    print_line(integer)
    print_line(string1)
    print_line(string2)
    print_line(floatingNumber)
    print_line(boolean)
    print_line(lst)
    print_line(dictionary)
    print_line(tupl)
    print_line(emptySet)


if __name__ == '__main__':
    my_var()
