#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.

"""

def main():
    from sys import argv
    from urllib import request
    from urllib import parse

    url, email = argv[1], argv[2]
    data = parse.urlencode({'email': email})
    data = data.encode('ascii')
    with request.urlopen(url, data) as f:
        print(f.read().decode('utf-8'))

if __name__ == '__main__':
    main()
