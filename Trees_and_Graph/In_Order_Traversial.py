__author__ = 'SunnyYan'

from Stacks_and_Queues.Stack import Stack
from Tree import BinarySearchTree

def inOrderTraversial(root):
    arraylist = []
    buffer = Stack()
    node = root
    buffer.push(node)
    node = node.leftChild
    while(node != None):
        buffer.push(node)
        node = node.leftChild

    while(buffer.isEmpty() is False):
        node = buffer.pop()
        arraylist.append(node.key)
        if(node.rightChild != None):
            node = node.rightChild
            while(node != None):
                buffer.push(node)
                node = node.leftChild

    return arraylist


# Testing part...
TreeRoot = BinarySearchTree()
Treelist = [10,5,3,4,7,6,8,11]

for i in Treelist:
    TreeRoot.insertion(i)

TreeRoot.root.printSubtree(5)

result = inOrderTraversial(TreeRoot.root)
print result
