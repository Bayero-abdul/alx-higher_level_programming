#!/usr/bin/python3
"""Lists 10 commits (from the most recent to oldest) of the
repository "rails" by the user “rails”

"""


if __name__ == '__main__':
    import sys
    import requests

    user, repo = sys.argv[1], sys.argv[2]
    r = requests.get(f'https://api.github.com/repos/{user}/{repo}/commits')
    author_commit = r.json()[:10]

    for commit in author_commit:
        print(f"{commit.get('sha')}:", end=" ")
        print(commit.get('commit').get('author').get('name'))
