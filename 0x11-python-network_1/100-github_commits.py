#!/usr/bin/python3
"""Lists 10 commits (from the most recent to oldest) of the
repository "rails" by the user “rails”

"""


if __name__ == '__main__':
    import sys
    import requests

    user, repo = sys.argv[1], sys.argv[2]
    r = requests.get(f"https://api.github.com/repos/{user}/{repo}/commits")
    commits = r.json()[:10]

    for commit in commits:
        print('{}: {}'.format(commit.get('sha'),
              commit.get('commit').get('author').get('name')))
