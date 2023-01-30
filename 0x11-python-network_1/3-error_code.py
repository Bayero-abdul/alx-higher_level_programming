#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response."""


def main():
    from sys import argv
    from urllib.request import urlopen
    from urllib.error import URLError, HTTPError

    url = argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)


if __name__ == '__main__':
    main()
