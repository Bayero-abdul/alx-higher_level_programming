#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response
using the requests module.

"""


def main():
    import requests
    from sys import argv

    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 200:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)


if __name__ == '__main__':
    main()
