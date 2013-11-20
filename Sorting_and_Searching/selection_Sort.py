__author__ = 'SunnyYan'

# Implement selection sort

def selectionSort(array):
    for i in range(0,len(array)):
        minValue = array[i]
        minIndex = i
        for j in range(i+1,len(array)):
            if(array[j] <= minValue):
                minValue = array[j]
                minIndex = j

        temp = array[i]
        array[i] = minValue
        array[minIndex] = temp

    return array


# Testing Part...

list = [6,5,4,3,2,1]
print list
result = selectionSort(list)

print result
