__author__ = 'SunnyYan'
# Write code to remove duplicates from an unsorted linked list
# Follow up
# How would you solve this problem if a temporary buffer is not allowed

from SingleLinkedList import SLinkedList


def findDuplicates(List):
    currentNode = List.head
    while(currentNode != None):
        runner = currentNode
        while(runner.next != None):
            if(currentNode.item == runner.next.item):
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next



# Testing Part:

T1 = SLinkedList()
for i in [1,2,3,3,4,4,5,5,6,6,6]:
    T1.insertBack(i)
print "We can find out the original single linkedlist is: " + str(T1.printList())
findDuplicates(T1)
print "After deleted the duplicated number of the list: " + str(T1.printList())