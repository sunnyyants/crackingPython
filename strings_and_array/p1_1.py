__author__ = 'SunnyYan'
# Implement an algorithm to determine if a string has all
# unique characters. What if you cannot use additional
# data structures?

from array import *

def findDuplicatedString(strings):
    result = [None]*95
    i = len(strings)-1
    while(i >= 0):
        val = ord(strings[i])-32
        if result[val] == 0:
            return "there is a duplicated word in strings\n"
        result[val] = 0
        i -= 1
    return "there isn't any duplicated word in strings\n"



print findDuplicatedString("anc")

print findDuplicatedString("anny")

print findDuplicatedString(("abcdeflji;aknclaknapeoja"))

print findDuplicatedString("abcdef")