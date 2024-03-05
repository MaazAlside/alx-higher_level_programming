#!/usr/bin/python3
""" POST Script to send email """
import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = sys.argv[1]
    email_value = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(email_value).encode('ascii')

    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
