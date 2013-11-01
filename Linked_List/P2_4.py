__author__ = 'SunnyYan'

# Write code to partition a linked list around a value x, such that all node
# less than x come before all nodes greater or equal to x

from SingleLinkedList import SLinkedList

def partition(LIST, value):
    lessBegin = SLinkedList()
    greaterBegin = SLinkedList()
    currentNode = LIST.head
    while(currentNode != None):
        if(currentNode.item < value):
            lessBegin.insertBack(currentNode.item)
        else:
            greaterBegin.insertBack((currentNode.item))
        currentNode = currentNode.next

    lessEnd = lessBegin.tail
    greaterEnd = greaterBegin.tail
    greaterEnd.next = None
    lessEnd.next = greaterBegin.head
    LIST.head = lessBegin.head


# Testing Part...

T4 = SLinkedList()
for i in range(0,5):
    T4.insertBack(i)
for j in range(1,8):
    T4.insertFront(j)

print "The original Single linked list is: " +(str)(T4.printList())

print "After partition..."

partition(T4,3)
print (str)(T4.printList())