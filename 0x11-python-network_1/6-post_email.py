#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response using the requests module.

"""


def main():
    from sys import argv
    import requests

    url, email = argv[1], argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)


if __name__ == '__main__':
    main()
