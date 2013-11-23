__author__ = 'SunnyYan'

# Implement of counting sort

def countingSort(array):
    c = [0] * (max(array) + 1)
    b = [0] * len(array)

    for i in range(0,len(array)):
        c[array[i]] += 1

    total = 0
    for i in range(0,len(c)):
        count = c[i]
        c[i] = total
        total += count

    for i in range(0,len(array)):
        b[c[array[i]]] = array[i]
        c[array[i]] += 1

    return b

# Testing Part...
array = [2,3,4,4,2,3,1,5,5,2,3,6,7,7,3,2]
result = countingSort(array)
print result