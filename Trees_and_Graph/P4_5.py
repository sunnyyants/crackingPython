__author__ = 'SunnyYan'

# Implement a function to check if a binary tree is a binary search tree.

from Tree import BinarySearchTree
from P4_3 import miniHeightBST
from Stacks_and_Queues.Stack import Stack

def checkBST(root):
    list = []
    stack = Stack()
    node = root
#    stack.push(node)
    while(stack.isEmpty() is False or node != None):
        if(node != None):
            stack.push(node)
            node = node.leftChild
        else:
            node = stack.pop()
            list.append(node.key)
            node = node.rightChild
    print list
    return checkOrder(list)


def checkOrder(list):
    while(len(list) != 1):
        buffer = list.pop()
        if(buffer < max(list)):
            return False
    return True




T5 = BinarySearchTree();
list = [1,2,3,4,5]
T5.root = miniHeightBST(list,0,len(list) - 1)
T5.root.printSubtree(5)


print (checkBST(T5.root) and "True") or "False"