#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.

"""


def main():
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers['X-Request-Id'])


if __name__ == '__main__':
    main()
