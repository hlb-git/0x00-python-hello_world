#!/usr/bin/python3
"""script to fetch a url with urllib library"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as response:
        content = response.read()
        msg = content.decode('utf-8')
        type = type(response.read())
        print("Body response:")
        print("\t- type: {}".format(type))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(msg))
