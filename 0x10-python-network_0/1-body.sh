#!/bin/bash
# script that takes in a URL, sends a GET request to the
curl -sI "$1" | grep -i 'HTTP/1.1 200' > /dev/null && curl -s "$1"
