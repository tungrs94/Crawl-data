import json
import sys

import requests


def get_repos(user):
    '''Get all GitHub repositories of user
    '''
    r = requests.get("http://api.github.com/users/{}/repos".format(user))
    data = json.loads(r.text)
    repos = [item['name'] for item in data]

    return repos


def main():
    user = sys.argv[1]
    repos = get_repos(user)
    print("GitHub User: {} has {} repositories:"
          .format(user, len(repos)))
    for repo in repos:
        print("-", repo)


if __name__ == "__main__":
    main()
