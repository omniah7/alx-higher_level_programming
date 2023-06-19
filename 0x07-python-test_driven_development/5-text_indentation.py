#!/usr/bin/python3
""" text_indentation Function """


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    space = True
    for c in text:
        if c is ' ' and space is True:
            continue
        space = False
        print(c, end='')
        if c in '.?:':
            print('\n')
            space = True
