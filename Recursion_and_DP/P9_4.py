__author__ = 'SunnyYan'

# Write a method to return all subsets of a set.

def getsubsets(set):
    allsubset = []
    max = 1 << len(set)
    for i in range(0,max):
        subset = converIntToSet(i, set)
        allsubset.append(subset);
    return allsubset

def converIntToSet(x,set):
    subset = []
    index = 0
    while(x > 0):
        if((x & 1) == 1):
            subset.append((set[index]))
        index += 1
        x = x >> 1

    return subset

# testing part...
set = [1,2,3]
allsubset = getsubsets(set)
set2 = [1,2,3,4]
allsubsets = getsubsets(set2)
print allsubset
print allsubsets
