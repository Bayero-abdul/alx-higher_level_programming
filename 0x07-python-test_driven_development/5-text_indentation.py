#!/usr/bin/python3
"""Module contain text_indentation() function."""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters:
, ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n\t")
    text = text.replace("?", "?\n\t")
    text = text.replace(":", ":\n\t")

    text = "\n\n".join([sentence.strip() for sentence in text.split("\n\t")])
    print(text.strip(), end ="")
