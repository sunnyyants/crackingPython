__author__ = 'SunnyYan'
# Implement an algorithm to find the kth to the last element of single
# Linked List

from SingleLinkedList import SLinkedList
def findtheNthtoLast(head, count, num):
    if(head is None):
        return head
    else:
        count += 1
        n = findtheNthtoLast(head.next, count, num)
        if(count is num):
            return head;
        return n

def findtheNthtoLast2(head, num):
    for i in range(1,num):
        head = head.next
    return head


# Testing part:
T2 = SLinkedList()
for i in range(0,10):
    T2.insertBack(i)

print "The original single linked list is: " + str(T2.printList())
print "We want to find the 3rd to last elements in the single linked list..."

T2.head = findtheNthtoLast(T2.head,0,2)
print "The result is: " +str(T2.printList())
T2.head = findtheNthtoLast2(T2.head,2)
print "The result is: " +str(T2.printList())