#!/usr/bin/python3
for letter in range(ord('a'), ord('z')):
    if letter == 'q':
        continue
    elif letter == 'e':
        continue
    else:
        print(chr(letter), end="")
