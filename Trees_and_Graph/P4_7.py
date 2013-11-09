__author__ = 'SunnyYan'

# Design an algorithm and write code to find the first common ancestor of two nodes
# in a binary tree. Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree.

from Tree import BinarySearchTree
from P4_3 import miniHeightBST

def findSide(root,target):
    if(root == None):
        return False
    if(root == target):
        return True
    return (findSide(root.leftChild,target) or findSide(root.rightChild,target))

def findCommonAncestor(root, node1, node2):
    if(root == None):
        return None
    if(node1 == root or node2 == root):
        return root

    IntheLeft = findSide(root.leftChild,node1)
    IntheRight = findSide(root.rightChild,node2)


    if(IntheLeft == IntheRight):
        return root

    if(IntheLeft): return findCommonAncestor(root.leftChild,node1,node2)
    elif(IntheRight): return findCommonAncestor(root.rightChild,node1,node2)


# Testing part...

list = [1,2,3,4,5,6,7,8,9,10]
T7 = BinarySearchTree()
T7.root = miniHeightBST(list, 0, len(list) - 1)
T7.root.printSubtree(5)

print "The common ancestor of node 1 and node 9 should be node 5: " + \
      str(findCommonAncestor(T7.root, T7.root.leftChild.leftChild, T7.root.rightChild.rightChild).key)
print "The common ancestor of node 7 and node 9 should be node 8: " + \
      str(findCommonAncestor(T7.root, T7.root.rightChild.leftChild.rightChild, T7.root.rightChild.rightChild).key)
print "The common ancestor of node 1 and node 4 should be node 2: " + \
      str(findCommonAncestor(T7.root, T7.root.leftChild.leftChild, T7.root.leftChild.rightChild.rightChild).key)