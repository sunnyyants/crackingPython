__author__ = 'SunnyYan'


# You have two very large binary trees: T1, with millions of nodes, and T2, with
# hundreds of nodes. Create an algorithm to decide if T2 is a subtree of T1.
# A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n
# is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.

from Tree import BinarySearchTree
from P4_3 import miniHeightBST

def containTree(T1, T2):
    if(T2 == None):
        return True
    return subTree(T1,T2)

def subTree(T1,T2):
    if(T1 == None):
        return False
    if(T1.key == T2.key):
        if(Check(T1,T2)):
            return True

    return subTree(T1.leftChild,T2) or subTree(T1.rightChild,T2)

def Check(T1,T2):
    if(T1 == None and T2 == None):
        return True
    if(T1 == None or T2 == None):
        return False
    if(T1.key != T2.key):
        return False
    return Check(T1.leftChild,T2.leftChild) and Check(T1.rightChild, T2.rightChild)

# Testing part...

T8_0 = BinarySearchTree()
T8_1 = BinarySearchTree()
T8_2 = BinarySearchTree()

print "Tree 0:"
list0 = [1,2,3,4,5,6,7,8,9,10]
T8_0.root = miniHeightBST(list0,0,len(list0)-1)
T8_0.root.printSubtree(5)

list1 = [2,1,3,4]
for i in list1:
    T8_1.insertion(i)
print "Tree 1: "
T8_1.root.printSubtree(5)

print "Tree 2:"
list2 = [8,6,7]
for j in list2:
    T8_2.insertion(j)
T8_2.root.printSubtree(5)

print "----------Checking-----------"
print "T1 is a subtree of T0 should be True: " + (containTree(T8_0.root,T8_1.root) and "True" or "False")
print "T2 is a subtree of T0 should be False: " + (containTree(T8_0.root,T8_2.root) and "True" or "False")