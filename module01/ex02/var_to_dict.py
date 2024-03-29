#!/usr/bin/python3

def transform_data_to_dictionary(d):
    keysList = [x[0] for x in d]
    valueList = [x[1] for x in d]
    dictionary = dict(zip(valueList, keysList))
    return dictionary


def print_dictionary(dictionary):
    for i in dictionary:
        print(i, ':', dictionary[i])


if __name__ == '__main__':
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]

    dictionary = transform_data_to_dictionary(d)
    print_dictionary(dictionary)
