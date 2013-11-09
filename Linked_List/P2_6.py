__author__ = 'SunnyYan'

# Given a circular linked list, implement algorithm which return the node
# at the beginning of the loop

from Linked_List.SingleLinkedList import SLinkedList


def findtheLoopStart(list):
    slow = list.head
    fast = list.head

    while(True):
        if(fast is None and fast.next is None):
            return None
            # There is any loop in the linked list
        slow = slow.next
        fast = fast.next.next
        if(fast == slow): break


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