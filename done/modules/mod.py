# import random as rand
import keyword
from math import sqrt
from random import choice, randint
import helpers
import apples
import file1

print(choice(["Ronnie", "Richard", "Young"]))
print(randint(1, 100))

answer = sqrt(15129)
print(answer)

# def contains_keywords(*args):
#     for item in args:
#         if item.iskeyword(item):
#             return True
#         else:
#             return False

# contains_keywords("hello", "goodbye")

def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False

answer = contains_keyword("Hello", "goodbye")
print(answer)

print(helpers.lucky_number())

print(apples.apple())
print(file1.peel())