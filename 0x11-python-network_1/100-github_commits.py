#!/usr/bin/python3
"""fetch repo commits and author name"""
import requests
import sys


if __name__ == "__main__":
    headers = {'Accept': "application/vnd.github+json",
               'Authorization': 'Bearer' + sys.argv[1],
               'X-GitHub-Api-Version': "2022-11-28"}
    response = requests.get('https://api.github.com/repos/' + sys.argv[2] +
                            '/' + sys.argv[2] + '/commits',
                            headers=headers)

    commitList = response.json()[:10]
    for commit in commitList:
        for key, value in commit.items():
            if key == 'sha':
                print('{}: '.format(value), end='')
            elif key == 'commit':
                print('{}'.format(value.get('author').get('name')))
