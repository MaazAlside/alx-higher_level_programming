#!/usr/bin/python3
""" POST Script to send email """
import sys
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    url_value = sys.argv[2]
    
    req = urllib.request.Request(url, data=url_value.encode('utf-8'))
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
