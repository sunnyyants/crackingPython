__author__ = 'SunnyYan'

# You are given a binary tree in which each node contains a value
# Design an algorithm to print all paths sum to a given value. The
# path does not need to start or end at the root a leaf

from P4_3 import miniHeightBST

def findSum(node, sum, path, level):
    if(node == None):
        return None

    path[level] = node.key

    t = 0
    for i in range(level,-1,-1):
        t += path[i]
        if(t == sum):
            printPath(path,i,level)

    findSum(node.leftChild,sum,path,level + 1)
    findSum(node.rightChild,sum,path,level + 1)

    path[level] = 0


def printPath(path, start, end):
    for i in range(start,end+1):
        print(str(path[i]) + " "),
    print " "

def depth(node):
    if(node == None):
        return 0
    else:
        return 1 + max(depth(node.rightChild),depth(node.leftChild))

def findPaths(node, sum):
    Depth = depth(node)
    path = [0] * Depth
    findSum(node,sum, path,0)


# Testing Part...

list = [-1,-4,2,-1,2,3,-4,5,-6,2,8,9]
T9 = miniHeightBST(list,0,len(list) - 1)
T9.printSubtree(5)
findPaths(T9,5)