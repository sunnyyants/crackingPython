__author__ = 'SunnyYan'

# Implementation of Bubble sort

def BubbleSort(array):
    for i in range(0,len(array) - 1):
        for j in range(0,len(array) - i - 1):
            if(array[j] > array[j + 1]):
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array

# Testing Part...
list = [6,5,4,3,2,1]

result = BubbleSort(list)
print result