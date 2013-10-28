__author__ = 'SunnyYan'
# Given an image represented by an N*N matrix, where each pixel in
# the image is 4 bytes, write a method to rotate the image by 90
# degrees. Can you do this in place?

def rotatematrix(array,n):
    layer = 0
    while(layer < n):
    #for layer in range(0,n):
        layer =+ 1
        first = layer;
        last = n - 1 - layer
        i = first
        while(i < last):
        #for i in range(first,last):
            i =+ 1
            offset = i -first

            #save top
            top = array[first][i]

            #left -> top
            array[first][i] = array[last-offset][first]

            #bottom ->left
            array[last-offset][first] = array[last][last-offset]

            #right -> buttom
            array[last][last-offset] = array[i][last]

            #top -> right
            array[i][last] = top


