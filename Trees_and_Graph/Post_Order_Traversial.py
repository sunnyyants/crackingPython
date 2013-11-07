__author__ = 'SunnyYan'

from Stacks_and_Queues.Stack import Stack
from Tree import BinarySearchTree

def postOrderTraversial(root):
    buffer = Stack()
    arraylist = []
    node = root
    buffer.push(node)
    node = node.leftChild
    while(node != None):
        buffer.push(node)
        node = node.leftChild

    while(buffer.isEmpty() is False):
        node = buffer.peek()
        if(node.rightChild != None and node.rightChild.visited is False): # We have to set a visited flag that make the
            node = node.rightChild                                        # nodes will not visit multiple times.
            while(node != None):
                buffer.push(node)
                parent = node
                node = node.leftChild

            if(parent.rightChild == None):
                arraylist.append(parent.key)
                parent.visited = True
                buffer.pop()
        else:
            node.visited = True                                          # Set visited flags
            arraylist.append(node.key)
            buffer.pop()
    return arraylist

#Testing part...
TreeRoot = BinarySearchTree()
Treelist = [10,5,3,4,7,6,8,11,12,9]

for i in Treelist:
    TreeRoot.insertion(i)

TreeRoot.root.printSubtree(5)

result = postOrderTraversial(TreeRoot.root)
print result