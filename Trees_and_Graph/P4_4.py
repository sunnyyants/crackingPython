__author__ = 'SunnyYan'


# Given a binary tree, design an algorithm which creates a linked list
# of all the nodes at each depth(e.g., if you have a tree with depth D,
# you'll have D linked lists


from Tree import BinarySearchTree
from P4_3 import miniHeightBST

def createLevelLinkedList(root, lists, level):

    if(root == None):
        return None
    if(len(lists) == level):
        linkedlist = []
        lists.append(linkedlist)
    else:
        linkedlist = lists[level]
    linkedlist.append(root.key)
    createLevelLinkedList(root.leftChild,lists,level+1)
    createLevelLinkedList(root.rightChild,lists,level+1)
    return lists




T4 = BinarySearchTree();
i = [1,2,3,4,5,6]
T4.root = miniHeightBST(i,0,len(i) - 1)

T4.root.printSubtree(5)
lists = []
result = createLevelLinkedList(T4.root, lists, 0)

for i in result:
    print i