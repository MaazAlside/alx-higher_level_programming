#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL """
import sys
import urllib.request

if __name__ = "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
