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
        for i in range(0,len(word)):
            substring = insertCharAt(word, firstcharacter, i)
            permutations.append(substring)

    return permutations

def insertCharAt(word, firstc, i):
    begin = word[0:i]
    end = word[i,len(word)]
    return (begin) + firstc + (end)





string = 'abcdefg'
print string[1:len(string)]