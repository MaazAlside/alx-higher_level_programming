#!/bin/bash
# Bash script to send a GET request to a URL
curl -sI "$1" | wc -c
