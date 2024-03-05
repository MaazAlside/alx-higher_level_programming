#!/usr/bin/python3
""" POST Script to send email """
import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = sys.argv[1]
    email_value = sys.argv[2]

    data = urllib.parse.urlencode({'email': email_value}).encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print("Your email is: " + response.read().decode('utf-8'))
