__author__ = 'SunnyYan'

# Implementation of Bubble sort

def BubbleSort(array):
    for i in range(0,len(array) - 1):
        for j in range(0,len(array) - i - 1):
            if(array[i] < array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array

# Testing Part...
list = [6,5,4,3,2,1]

result = BubbleSort(list)
print result