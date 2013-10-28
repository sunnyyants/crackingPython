__author__ = 'SunnyYan'
# Assume you have a isSubstring which check if one word is the substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only
# one call to isSubstring(e.g.,"waterbottle" is a rotation of "erbottlewat").

import pygame

def checkRotationString(string1, string2):
    length = len(string1)
    if length == len(string2) and len > 0:
        newstring = ''.join([string1, string1])
        # Replace the call of function isSubstring
        if newstring.find(string2,0,len(newstring)) != -1:
            return True
    return False

test = "waterbottle"
rotated = "erbottlewat"
rotated2 = "rrbottlewat"

print (checkRotationString(rotated, test))
print (checkRotationString(rotated2, test))
