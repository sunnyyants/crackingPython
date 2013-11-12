__author__ = 'SunnyYan'


# Imagine a robot sitting on the upper left corner of an X and Y grid
# The robot can only move in two direction: right and down. How many
# possible path are there for the robot to go from (0,0) to (X,Y)?

# Follow up
# Imagine certain spots are "off limits", such that the robot cannot
# step on them. Design an algorithm to find a path for the robot from
# the top left to the bottom right.

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def getPath(x,y,list,restrict):
    if(x == 0 and y == 0):
        return True
    success = False
    if(x >= 1 and isFree(x-1,y,restrict)):
        success = getPath(x-1,y,list,restrict)
    if(success == False and isFree(x,y-1,restrict)):
        success = getPath(x,y-1,list,restrict)
    if(success):
        p = Point(x,y)
        list.append(p)
    return success

def isFree(x,y,restrict):
    if(restrict[x][y] == 1):
        return False
    else:
        return True

# Testing Part...

print "Generated a 4*3 grid and set grid[0][1] gird[2][2] as off-limit"
row = [0,1,0]
matrix = [[0,0,0],[1,0,0],[0,0,1],[0,0,0]]

# [0 1 0 0]
#  |
# [0-0-0-0]
#        |
# [0 0 1 0]

list = []
getPath(3,2,list,matrix)
for i in list:
    print "[x: " + str(i.x),
    print "| y: " + str(i.y) + "]"

print "Total " +str(len(list)) + " steps"