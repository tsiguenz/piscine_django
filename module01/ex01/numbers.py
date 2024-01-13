#!/usr/bin/python3

def get_raw_content():
    try:
        with open("numbers.txt") as file:
            rawContent = file.read()
    except Exception as e:
        print(e)
        exit(1)
    return rawContent


def format_raw_content_to_number_list(rawContent):
    list = rawContent.split(',')
    try:
        formatedList = [int(x) for x in list]
    except Exception as e:
        print("Error:", e)
        exit(1)
    return formatedList


def print_list(content):
    for number in content:
        print(number)


if __name__ == '__main__':
    rawContent = get_raw_content()
    formatedList = format_raw_content_to_number_list(rawContent)
    print_list(formatedList)
