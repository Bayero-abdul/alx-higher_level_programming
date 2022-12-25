#!/usr/bin/python3
"""Lists 10 commits (from the most recent to oldest) of the
repository "rails" by the user “rails”

"""

"""
def main():
    from sys import argv
    import requests

    user, repo = argv[1], argv[2]
    r = requests.get(f'https://api.github.com/repos/{user}/{repo}/commits')
    commits = r.json()
    commit_list = commits[:10]
    
    for commit in commit_list:
        print('{}: {}'.format(commit.get('sha'),
              commit.get('commit').get('author').get('name')))


if __name__ == '__main__':
    main()
"""

if __name__ == '__main__':
    import sys
    import requests

    a = sys.argv[1:]
    coms = requests.get(f"https://api.github.com/repos/{a[1]}/{a[0]}/commits")
    top_ten = coms.json()[:10]

    for i in top_ten:
        print(f"{i.get('sha')}:", end=" ")
        print(i.get('commit').get('author').get('name'))
