#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response."""


def main():
    from sys import argv
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError

    url = argv[1]
    req = Request(url)
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('Error code: ', e.code)
    else:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    main()
