#!/bin/bash
# Bash script to send a GET request to a URL and display the size of the response body in bytes
curl -s -w "%{size_download}" -X GET "$1"
