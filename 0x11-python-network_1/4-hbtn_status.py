#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status."""


def main():
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print(f'Body response:\n\t\
- type: {type(r.text)}\n\t\
- content: {r.text}')


if __name__ == '__main__':
    main()
