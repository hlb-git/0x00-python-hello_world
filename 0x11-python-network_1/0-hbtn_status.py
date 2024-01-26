#!/usr/bin/python3
"""script to fetch a url with urllib library"""
import urllib.request


request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(request) as response:
    content = response.read()
    output = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}
    """.format(type(content), content,
               content.decode('utf-8'))
    output = output.rstrip()
    print(output)
