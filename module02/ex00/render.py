#!/usr/bin/python3

import settings
import sys
import os

def get_html_squeleton():
    template = '<!DOCTYPE html>\n'
    template += '<html lang="en">\n'
    template += '   <head>\n'
    template += '       <meta charset="UTF-8">\n'
    template += '       <title>{title}</title>\n'
    template += '   </head>\n'
    template += '   <body>\n'
    template += '{body}'
    template += '   </body>\n'
    template += '</html>\n'
    return template


def get_var_list(raw):
    lst = []
    while True:
        o_brace = raw.find('{')
        c_brace = raw.find('}')
        if o_brace == -1 or c_brace == -1:
            return lst
        lst.append(raw[o_brace+1:c_brace])
        raw = raw[c_brace + 1:]


def get_html_file_name(template_file_name):
    splited_template_file_name = template_file_name.split('.')
    if len(splited_template_file_name) < 2 or splited_template_file_name[-1] != 'template':
        print(f'Bad template name.\n{USAGE}')
        exit(1)
    return template_file_name[0:template_file_name.rfind('.')] + '.html'


def get_template_content(template_file_name):
    try:
        with open(template_file_name, 'r') as file:
            return file.read()
    except Exception as e:
        print('Error while opening file:', e)
        exit(1)


def replace_var_by_value(raw, settings):
    for var in var_list:
        raw = raw.replace("{" + var + "}", settings.__dict__[var])
    return raw


def write_to_file(html, path):
    try:
        with open(path, 'w') as file:
            return file.write(html)
    except Exception as e:
        print('Error while opening file:', e)
        exit(1)


if __name__ == '__main__':
    USAGE = 'Usage: python3 render.py <file.template>'
    if len(sys.argv) != 2:
        print(USAGE)
        exit(1)
    template_file_name = sys.argv[1]
    html_file_name = get_html_file_name(template_file_name)
    title = os.path.basename(html_file_name).rstrip('.html')
    template_content = get_template_content(template_file_name)
    var_list = get_var_list(template_content)
    formated_str = replace_var_by_value(template_content, settings)
    html_squeleton = get_html_squeleton()
    html = html_squeleton.format(title=title, body=formated_str)
    write_to_file(html, html_file_name)
