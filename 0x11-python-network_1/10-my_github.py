#!/usr/bin/python3
"""takes varible in json format"""
import requests
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    headers = {'Authentication': 'Bearer' + password}

    response = requests.get("https://api.github.com/users/{}".format(username),
                            headers=headers)
    if response.status_code == 200:
        id = response.json().get('id')
        print(id)
    else:
        print("None")
