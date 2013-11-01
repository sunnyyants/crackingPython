__author__ = 'SunnyYan'

# Given a circular linked list, implement algorithm which return the node
# at the beginning of the loop

from SingleLinkedList import SLinkedList
from SingleLinkedList import SNode

def findtheLoopStart(list):
    slow = list.head.next
    fast = list.head.next.next

    while(slow != fast):
        slow = slow.next
        fast = fast.next.next

    # There is any loop in the linked list
    if(slow == None or fast == None):
        return None

    # Find out the start point of the loop linked list from the meet point.
    slow = list.head
    while(slow != fast):
        slow = slow.next
        fast = fast.next

    return slow

# Testing part...

T6 = SLinkedList()
for i in range(0,16):
    T6.insertBack(i)

find = T6.head
while(find.item != 4):
    find = find.next

T6.tail.next = find

print "The start of the loop in linked list should be 4: " + (str)(findtheLoopStart(T6).item)