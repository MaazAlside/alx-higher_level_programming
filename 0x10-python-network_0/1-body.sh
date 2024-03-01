#!/bin/bash
# script that takes in a URL, sends a GET request to the
curl -L -sI -X HEAD -w "%{http_code}" "$1" | grep -q '^200' && curl -Ls "$1"
