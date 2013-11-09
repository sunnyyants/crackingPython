__author__ = 'SunnyYan'

# Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.

from Tree import BinarySearchTree
from Tree import TreeNode

def miniHeightBST(item, start, end):
    if(start > end):
        return None
    mid = (start + end) / 2
    n = TreeNode(None,item[mid])
    n.leftChild = miniHeightBST(item,start,mid-1)
    n.rightChild = miniHeightBST(item,mid+1,end)
    return n

# Testing part...

list = [1,2,3,4,5,6,7,8,9,10]


root = miniHeightBST(list,0,len(list) - 1)

root.printSubtree(5)