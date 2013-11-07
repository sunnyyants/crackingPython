__author__ = 'SunnyYan'

from Stacks_and_Queues.Stack import Stack
from Tree import BinarySearchTree
def preOrderTraversial(root):
    arraylist = []
    buffer = Stack()
    node = root
    arraylist.append(node.key)
    buffer.push(node)
    node = node.leftChild
    while(node != None):
        buffer.push(node)
        arraylist.append(node.key)
        node = node.leftChild

    while(buffer.size != 0):
        node = buffer.pop()
        if(node.rightChild != None):
            node = node.rightChild
            while(node != None):
                buffer.push(node)
                arraylist.append(node.key)
                node = node.leftChild


    return arraylist

# Testing part...

TreeRoot = BinarySearchTree()
treekeylist = [10,5,11,3,7,4,6,8]
for i in treekeylist:
    TreeRoot.insertion(i)

TreeRoot.root.printSubtree(5)
TreeList = preOrderTraversial(TreeRoot.root)
print TreeList

