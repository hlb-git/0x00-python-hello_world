#!/usr/bin/python3
"""sends email to url from command line"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        page = response.read().decode('utf-8')
        print(page)
