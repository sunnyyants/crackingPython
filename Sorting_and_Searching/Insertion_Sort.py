__author__ = 'SunnyYan'

# Implementation of insertion sort...

def insertionSort(array):
    for i in range(1,len(array)):
        index = i-1;
        buffer = array[i];
        while(buffer < array[index] and index >= 0):
            array[index+1] = array[index]
            index -= 1
        array[index+1] = buffer

    return array


# Testing part...

list = [5,4,3]
result = insertionSort(list)
print result