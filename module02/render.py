#!/bin/env python3

import settings
import os
import sys

def get_param_list(raw):
    lst = []
    while True:
        o_brace = raw.find('{')
        c_brace = raw.find('}')
        if o_brace == -1 or c_brace == -1:
            return lst
        lst.append(raw[o_brace+1:c_brace])
        raw = raw[c_brace + 1:]


if __name__ == '__main__':
    USAGE = 'Usage: python3 render.py <file.template>'
    if len(sys.argv) != 2:
        print(USAGE)
        exit(1)
    template_file_name = sys.argv[1]
    splited_template = template_file_name.split('.')
    if len(splited_template) < 2 or splited_template[-1] != 'template':
        print(f'Bad template name.\n{USAGE}')
        exit(1)
    html_file = template_file_name[0:template_file_name.rfind('.')] + '.html'
    try:
        with open(template_file_name) as file:
            raw = file.read()
    except Exception as e:
        print('Error while opening file:', e)
        exit(1)
    param_list = get_param_list(raw)
    print(raw.format(name = settings.__dict__[param_list[0]]))
