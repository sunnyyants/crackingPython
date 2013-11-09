__author__ = 'SunnyYan'

# Write an algorithm to find the 'next' node (i.e., in-order successor) of a
# given node in a binary search tree. You may assume that each node has a link
# to its parent.

from Tree import BinarySearchTree

def findInorderSuccessor(node):
    if(node == None):
        return None
    if(node.rightChild != None):
        node = node.rightChild
        while(node.leftChild != None):
            node = node.leftChild

        return node
    else:
        current = node
        parent = node.parent
        while(parent != None and parent.leftChild != current):
            current = parent
            parent = current.parent

        return parent

# Testing Part...

T6 = BinarySearchTree()
Treelist = [10,5,3,4,7,6,8,11]

for i in Treelist:
    T6.insertion(i)


T6.root.printSubtree(5)
print "The in order successor of node 7 should be 8: " + \
      str(findInorderSuccessor(T6.root.leftChild.rightChild).key)
print "The in order successor of node 4 should be 5: " + \
      str(findInorderSuccessor(T6.root.leftChild.leftChild.rightChild).key)

