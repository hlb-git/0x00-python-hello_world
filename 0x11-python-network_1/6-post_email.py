#!/usr/bin/python3
"""post email to a server using the header variable"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1], data={'email': sys.argv[2])
    print(response.text)
