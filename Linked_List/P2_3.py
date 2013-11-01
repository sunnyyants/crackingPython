__author__ = 'SunnyYan'
# Implement an algorithm to delete a node in the middle of a
# single linked list, given only access to that node.

from SingleLinkedList import SLinkedList

def deletemiddleNode(node):
    while(node.next != None):
        node.item = node.next.item
        node = node.next
    node.item = None

# Testing part:

T3 = SLinkedList()
for i in range(1,6):
    T3.insertBack(i)

print "The original single linked list is: " +str(T3.printList())
print "After deleted the middle one: (and we make the last node dummy)"
deletemiddleNode(T3.head.next.next)
print str(T3.printList())