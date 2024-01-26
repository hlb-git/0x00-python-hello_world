#!/usr/bin/python3
"""print value in http header file"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    id = response.headers.get('X-Request-Id')
    print(id)
