__author__ = 'SunnyYan'

# You have two numbers represented by a linked list, where each node contains a
# single digit. The digits are stored in reverse order, such that the 1's digit i
# sat the head of the list. Write a function that adds the two numbers and returns
# the sum as a linked list.

from Linked_List.SingleLinkedList import SLinkedList
from Linked_List.SingleLinkedList import SNode

def addList(listnode1, listnode2, carry):
    if(listnode1 == None and listnode2 == None and carry == 0):
        return None

    result = SNode(carry,None)
    value = carry

    if(listnode1 != None):
        value += listnode1.item

    if(listnode2 != None):
        value += listnode2.item

    result.item = value % 10
    # recursion...
    if(listnode1 != None or listnode2 != None):
        next = addList(((listnode1 == None) and None or listnode1.next),
                       ((listnode2 == None) and None or listnode2.next), value / 10)
        result.next = next
    return result


# Testing part:

L5 = SLinkedList();
L6 = SLinkedList();
L7 = SLinkedList();
for i in range(7,10):
    L5.insertBack(i)
for j in range(3,6):
    L6.insertBack(j)

print "The original L5 is: " + (str)(L5.printList())
print "The original L6 is: " + (str)(L6.printList())

L7.head = addList(L5.head,L6.head,0)

print "After summation L7 is: " + (str)(L7.printList())

# Follow up
# Suppose the digits are stored in the forward order, repeat the question

