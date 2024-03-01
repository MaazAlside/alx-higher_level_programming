#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL
curl -s -X POST -d "email=test@gmail.com&subject=I_will_always_be_here_for_PLD" "$1"
