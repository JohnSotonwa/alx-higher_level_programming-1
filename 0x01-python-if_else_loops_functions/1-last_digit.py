#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is {} ".format(number, repr(number)[-1]), end="")

if int(repr(number)[-1]) > 5:
    print("and is greater than 5")
elif int(repr(number)[-1]) == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
