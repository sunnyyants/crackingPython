__author__ = 'SunnyYan'
# Give two strings, write a method to decide if one is
# a permutation of the other
# there is a method which is sort the string and figure out
# whether these two strings are identity.
# But this kind of method is not quite good.
def findPermutation(a,b):
    if len(a) != len(b):
        return False
    letter = [0]*95
    i = 0
    while(i < len(a)):
        letter[ord(a[i])-32] += 1
        i += 1
    j = 0
    while(j < len(b)):
        letter[ord(b[j])-32] -= 1
        if letter[ord(b[j])-32] < 0:
            return False
        j += 1

    return True


testA = "abcdefg"
testB = "abcefdg"
testC = "alkejico"
testD = "abcdef"

# cond ? a:b
print (findPermutation(testA,testB) and True) or False
print (findPermutation(testB,testC) and True) or False
print (findPermutation(testC,testD) and True) or False

# fix the flaw of cond ? a:b
a,b=1,0
print (False and [a] or [b])[0]