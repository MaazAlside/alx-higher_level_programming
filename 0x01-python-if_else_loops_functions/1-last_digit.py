#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = int(repr(number)[-1])
start_text = "Last digit of"
if (last_number > 5):
    print("{} {} is {} and is greater than 5"
          .format(start_text, number, last_number))
elif (last_number == 0):
    print("{} {} is {} and and is 0"
          .format(start_text, number, last_number))
elif (last_number < 6 and last_number != 0):
    print("{} {} is {} and is less than 6 and not 0"
          .format(start_text, number, last_number))
