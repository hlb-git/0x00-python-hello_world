#!/usr/bin/python3
"""print the request id in the header section"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        id = response.headers.get('X-Request-Id')
        print(id)
