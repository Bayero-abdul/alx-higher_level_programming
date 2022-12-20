#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response using
requests module.

"""


def main():
    import sys
    import requests

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])


if __name__ == '__main__':
    main()
