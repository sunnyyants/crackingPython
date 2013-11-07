__author__ = 'SunnyYan'

from Stacks_and_Queues.Stack import Stack
from Tree import BinarySearchTree

def postOrderTraversial(root):
    buffer = Stack()
    arraylist = []
    node = root
    buffer.push(node)
    node = node.leftChild
    while(node.leftChild != None):
        buffer.push(node)
        node = node.leftChild
    arraylist.append(node.key)
    buffer.push(node)
    while(buffer.isEmpty() is False):
        node = buffer.pop()
        #arraylist.append(node.key)
        if(node.rightChild != None):
            node = node.rightChild
        while(node != None):
            buffer.push(node)
            node = node.leftChild
            
