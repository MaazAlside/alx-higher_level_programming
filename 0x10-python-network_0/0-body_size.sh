#!/bin/bash
# Bash script 
body_size=$(curl -s -w "%{size_download}" -X GET "$1")
echo "$body_size"
