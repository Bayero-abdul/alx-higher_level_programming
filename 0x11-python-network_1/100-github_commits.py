#!/usr/bin/python3
"""Lists 10 commits (from the most recent to oldest) of the
repository "rails" by the user “rails”

"""


def main():
    from sys import argv
    import requests

    user, repo = argv[1], argv[2]
    r = requests.get(f'https://api.github.com/repos/{user}/{repo}/commits')
    commit_list = r.json()
    for commit in commit_list[0:10]:
        print('{}: {}'.format(commit['sha'],
              commit['commit']['author']['name']))


if __name__ == '__main__':
    main()
