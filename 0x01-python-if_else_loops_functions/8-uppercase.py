#!/usr/bin/python3
def uppercase(str):
    new = ""
    for character in str:
        new += "%c" % to_uper(character)
    print("{:s}".format(new))
