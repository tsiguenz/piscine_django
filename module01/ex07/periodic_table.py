#!/usr/bin/python3


def line_to_clean_list(line):
    line = line.replace(':', ' ')
    line = line.replace(',', ' ')
    line = line.split()
    return line


def parse_line(line):
    line = line_to_clean_list(line)
    name = line[0]
    position = int(line[3])
    number = line[5]
    small = line[7]
    molar = line[9]
    return {'name': name, 'position': position, 'number': number,
            'small': small, 'molar': molar}


def parse_txt():
    elements = list(dict())
    try:
        with open('periodic_table.txt') as file:
            for line in file:
                elements.append(parse_line(line))
    except Exception as e:
        print('Error while reading txt file:', e)
        exit(1)
    return elements


def get_html_table_data(element):
    data = '      <td class="elemBox">\n'
    data += f'          <h4>{element.get("name")}</h4>\n'
    data += '          <ul>\n'
    data += f'              <li><h4>{element.get("number")}</h4></li>\n'
    data += f'              <li><h1>{element.get("small")}</h1></li>\n'
    data += f'              <li>{element.get("molar")}</li>\n'
    data += '          </ul>\n'
    data += '      </td>\n'
    return data


def get_html_table(elements):
    table = '<table>\n'
    table += '  <thead>\n'
    table += '      <tr>\n'
    for i in range(1, 19):
        table += f'      <td class="colIndex">{i}</td>\n'
    table += '      </tr>\n'
    table += '  </thead>\n'
    table += '  <tr>\n'
    pos = 0
    for elem in elements:
        currentPos = elem.get('position')
        if currentPos < pos:
            table += '  </tr>\n'
            table += '  <tr>\n'
            pos = currentPos
        while pos < currentPos:
            table += '      <td>\n'
            table += '      </td>\n'
            pos += 1
        table += get_html_table_data(elem)
        pos += 1
    table += '  </tr>\n'
    table += '</table>\n'
    return table


def get_style():
    style = 'ul {\n'
    style += '	list-style: none;\n'
    style += '	padding: 0;\n'
    style += '	margin: 2px;\n'
    style += '	text-align: center;\n'
    style += '}\n'
    style += '\n'
    style += 'li {\n'
    style += '	font-size: xx-small;\n'
    style += '}\n'
    style += '\n'
    style += 'h1 {\n'
    style += '	margin: 5px;\n'
    style += '}\n'
    style += '\n'
    style += 'h4 {\n'
    style += '	padding: 0;\n'
    style += '	padding-top: 2px;\n'
    style += '	margin: 2px;\n'
    style += '	text-align: center;\n'
    style += '	font-size: small;\n'
    style += '}\n'
    style += '\n'
    style += '.colIndex {\n'
    style += '	text-align: center;\n'
    style += '}\n'
    style += '\n'
    style += '.elemBox {\n'
    style += '	border: 1px solid black;\n'
    style += '	padding: 0;\n'
    style += '}\n'
    return style


def get_html(elements):
    style = get_style()
    template = get_html_template()
    htmlTable = get_html_table(elements)
    html = template.format(style, htmlTable)
    return html


def get_html_template():
    template = '<!DOCTYPE html>\n'
    template += '<html lang="en">\n'
    template += '   <head>\n'
    template += '       <meta charset="UTF-8">\n'
    template += '       <style>\n'
    template += '{}'
    template += '       </style>\n'
    template += '       <title> Periodic table </title>\n'
    template += '   </head>\n'
    template += '   <body>\n'
    template += '{}'
    template += '   </body>\n'
    template += '</html>'
    return template


def render_periodic_table():
    elements = parse_txt()
    html = get_html(elements)
    try:
        with open('periodic_table.html', 'w+') as file:
            file.write(html)
    except Exception as e:
        print('Error while opening html file:', e)
        exit(1)


if __name__ == '__main__':
    render_periodic_table()
