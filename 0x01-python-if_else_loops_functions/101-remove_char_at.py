#!/usr/bin/python3
def remove_char_at(str, n):
    """removing the character at the position n"""
    if n < 0 or n > len(str) - 1:
        return (str)
    if len(str) - 1 == n:
        return str[:n]
    else:
        str = str[:n] + str[n+1:]
        return (str)
