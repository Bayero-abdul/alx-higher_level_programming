#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and
uses the GitHub API to display your id.

"""


def main():
    from sys import argv
    import requests

    user, passwd = argv[1], argv[2]
    r = requests.get('https://api.github.com/user', auth=(user, passwd))
    json = r.json()
    print(json.get('id'))


if __name__ == '__main__':
    main()
