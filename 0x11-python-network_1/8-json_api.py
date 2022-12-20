#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

"""

def main():
    from sys import argv
    import requests

    data = {}
    try:
        data['q'] = argv[1]
    except:
        data['q'] = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    if r.headers['Content-Type'] == 'application/json' and r.json() != {}:
        json = r.json()
        print('[{}] {}'.format(json.get('id'), json.get('name')))
    else:
        if r.headers['Content-Type'] != 'application/json':
            print('Not a valid JSON')
        else:
            print('No result')


if __name__ == '__main__':
    main()
