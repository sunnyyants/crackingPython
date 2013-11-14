__author__ = 'SunnyYan'

# A magic index in an array A[1...n-1] is defined to an index such
# that A[i] = i. Given a sorted array in distinct integers,
# write a method to find a magic index, if one exists, in array A.

def findMagic(array, start, end):
    if(start > end or start < 0 or end > len(array)):
        return -1;

    mid = (start + end) / 2
    if(mid == array[mid]):
        return mid;
    if(mid > array[mid]):
        return findMagic(array, mid + 1, end)
    else:
        return findMagic(array, start, mid - 1)

# Follow up
# What if the value is not distinct
def findMagic2(array, start, end, result):
    if(start > end or start < 0 or end > len(array)):
        return -1;
    mid = (start + end) / 2
    if(mid == array[mid]):
        result.append(mid)

    findMagic2(array, start, mid - 1, result)
    findMagic2(array, mid + 1, end, result)


# Testing part...

list = [-5,-2,-1,0,2,4,6,8]
print "The magic index should be 6: " + str(findMagic(list,0,len(list) - 1))
list2 = [-10,-5,2,2,2,3,4,7,9,12,13]
result = []
findMagic2(list2, 0, len(list2)-1, result)
print "The magic index should be [2,7]: " + str(result)