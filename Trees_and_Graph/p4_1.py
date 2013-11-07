__author__ = 'SunnyYan'

# Implement a function to check if a binary tree is balanced. For the purposed
# of this question, a balance tree is defined to be a tree such that the heights
# of two subtrees of any node never differ by more than one.

from Tree import BinarySearchTree

def checkHeight(root):
    if(root == None):
        return 0

    leftHeight = checkHeight(root.leftChild)
    if(leftHeight == -1):
        return -1

    rightHeight = checkHeight(root.rightChild)
    if(rightHeight == -1):
        return -1

    difference = abs((leftHeight-rightHeight))
    if(difference > 1):
        return -1
    else:
        return max(leftHeight,rightHeight) + 1


def checkBalance(root):
    if(checkHeight(root) == -1):
        print "The tree is not balanced!"

    else:
        print "The height of tree is: " + str(checkHeight(root))

# Testing Part...
balance = [5,3,2,4,6]
unbalance = [5,3,2,4,6,1]

T1 = BinarySearchTree()
T2 = BinarySearchTree()
for i in balance:
    T1.insertion(i)
T1.root.printSubtree(5)
for i in unbalance:
    T2.insertion(i)
T2.root.printSubtree(5)

checkBalance(T1.root)
checkBalance(T2.root)
