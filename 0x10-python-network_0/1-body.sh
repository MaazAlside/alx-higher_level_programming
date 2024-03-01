#!/bin/bash
# script that takes in a URL, sends a GET request to the
curl -s -I "$1" | awk 'NR==1 && $2==200 {getline; print}' | curl -s "$1"
