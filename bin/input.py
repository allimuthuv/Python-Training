#!/bin/python

name = raw_input("What is your name? ")
birthdate = raw_input("What is your birthdate? ")
age = raw_input("How old are you? ")

print("%s born on %s" % (name,birthdate))
print("Half of your age is %s" % (int(age) / 2))
