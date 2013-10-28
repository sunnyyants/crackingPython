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
    print len(l)
    i = 1
    lenth = len(l) * 2 - 1
    while(i < lenth):
        l.insert(i,"%20")
        i += 2
    return ''.join(l)


testing = "Mr John Smith"
testing2 = "Hello everyone I am Sunny Yan"
print testing.split()
abc = testing.split()
print ''.join(testing.split())
print abc
print ''.join(abc)
print replacethespace(testing)
print replacethespace(testing2)