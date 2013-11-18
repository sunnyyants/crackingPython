__author__ = 'SunnyYan'

# Write a method to compute all the permutation of a string

def permutation(string):
    if string == None:
        return None

    permutations = []
    if(len(string) == 0):
        permutations.append("")
        return permutations

    firstcharacter = string[0]
    remainder = string[1:len(string)]
    words = permutation(remainder)
    for word in words:
        for i in range(0,len(word)+1):
            substring = insertCharAt(word, firstcharacter, i)
            permutations.append(substring)
    return permutations

def insertCharAt(word, firstc, i):
    begin = word[0:i]
    end = word[i:]
    return (begin) + firstc + (end)

def permute2(s):
    res = []
    if len(s) == 1:
        res = [s]
    else:
        for i, c in enumerate(s):
            #print "i:" + str(i)
            #print "c:" + str(c)
            for perm in permute2(s[:i] + s[i+1:]):
                res += [c + perm]


    return res

# Testing Part...
list = permutation("abc")
print list
print permute2("abc")


