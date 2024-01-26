#!/usr/bin/python3
"""handle url error with try and except"""
import urllib.request
import urllib.parse
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            page = response.read().decode('utf-8')
            print(page)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
