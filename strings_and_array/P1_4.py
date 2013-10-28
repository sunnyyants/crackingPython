__author__ = 'SunnyYan'
# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the
# end of the string to hold the additional characters, and
# that you are given the "true" length of the string.
# (Node: if implementing in Java, please use a character array
# so that you can perform this operation in place.)
# Example:
# Input:  "Mr John Smith    "
# Output: "Mr%20John%20Smith"

def replacethespace(string):
    l = string.split()
    length = len(l) * 2 - 1
    for i in range(1, length, 2):
        l.insert(i, "%20")
    return ''.join(l)


testing = "Mr John Smith"
testing2 = "Hello everyone I am Sunny Yan"
print testing
print replacethespace(testing)
print testing2
print replacethespace(testing2)

