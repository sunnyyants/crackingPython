__author__ = 'SunnyYan'
# Implement an algorithm to determine if a string has all
# unique characters. What if you cannot use additional
# data structures?

def findDuplicatedString(strings):
    result = [None]*95
    for i in range(0, len(strings)):
        val = ord(strings[i])-32
        if result[val] == 0:
            return "there is a duplicated word in strings\n"
        result[val] = 0
    return "there isn't any duplicated word in strings\n"



print findDuplicatedString("anc")

print findDuplicatedString("anny")

print findDuplicatedString(("abcdeflji;aknclaknapeoja"))

print findDuplicatedString("abcdef")