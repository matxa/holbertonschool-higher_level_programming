#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

module_ten = 10
if (number < 0):
    module_ten *= -1
last_digit = number % (module_ten)

if (last_digit > 5):
    print("Last digit of {:d} is {:d} \
    and is greater than 5".format(number, last_digit))
elif (last_digit == 0):
    print("Last digit of {:d} is {:d} \
    and is 0".format(number, last_digit))
elif (last_digit < 6 and last_digit != 0):
    print("Last digit of {:d} is {:d} \
    and is less than 6 and not 0".format(number, last_digit))
