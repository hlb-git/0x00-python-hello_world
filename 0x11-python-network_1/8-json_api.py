#!/usr/bin/python3
"""takes varible in json format"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        value = sys.argv[1]
    else:
        value = ""
    response = requests.post("http://0.0.0.0:5000/search_user",
                             data={'q': value})
    try:
        if response.json():
            print("[{}] {}".format(response.json().get('id'),
                                   response.json().get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
