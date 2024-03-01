#!/bin/bash
# Bash script to send a GET request to a URL
res=$(curl -s -o /dev/null -w  "%{size_download}" "$1")
echo "$res bytes"
