__author__ = 'SunnyYan'


# Define the Double LinkList Node class

class DNode:
    def __init__(self, item, prev, next):
        self.item = item
        self.prev = prev
        self.next = next

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def insertAfter(self, item):
        self.next = DNode(item,self,self.next)
        self.next.next.prev = self.next

    def insertBefore(self, item):
        self.prev = DNode(item,self.prev,self)
        self.prev.prev.next = self.prev

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

        self.next = None
        self.prev = None


# Double LinkedList class
# It's implementation is circularly-linked and employs sentinel
# at the head of the list

# Dlist invariants:
# 1) head != None
# 2) For every DListNode x in the DList, x.next != None.
# 3) For every DListNode x in the DList, x.prev != None.
# 4) For every DListNode x in the DList, if x.next == y, then y.prev == x
# 5) For every DListNode x in the DList, if x.prev == y, then y.next == x
# 6) size if the number of DListNodes, NOT COUNTING the sentinel,
#    that can be accessed from the sentinel (head) by a sequence of "next"
#    references

class DList:
    def __init__(self):
        self.head = DNode(None,None,None)
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0

    def insertFront(self, item):
        if(self.isEmpty()):
            self.head.next = DNode(item,self.head,self.head)
            self.head.prev = self.head.next
        else:
            self.head.next = DNode(item,self.head,self.head.next)
            self.head.next.next.prev = self.head.next
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def insertBack(self, item):
        if(self.isEmpty()):
            self.head.next = DNode(item, self.head,self.head)
            self.head.prev = self.head.next
        else:
            self.head.prev = DNode(item,self.head.prev,self.head)
            self.head.prev.prev.next = self.head.prev
        self.size += 1

    def getFront(self):
        return self.head.next

    def getBack(self):
        return self.head.prev

    def printList(self):
        self.result = []
        currentNode = self.head.next
        while(currentNode != self.head):
            self.result.append(currentNode.item)
            currentNode = currentNode.next
        return self.result

    def remove(self,item):
        currentNode = self.head.next
        while(currentNode != self.head):
            if(currentNode.item == item):
                currentNode.remove()
                self.size -= 1
                return
            currentNode = currentNode.next

    def poll(self):
        currentNode = self.head.next
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return currentNode

# testing the linked list
#
# l1 = DList()
#
# for i in range(0,10):
#     l1.insertBack(i)
# print "The LinkedList should be [0,1,2,3,4,5,6,7,8,9]: " + str(l1.printList())
#
#
# l2 = DList()
# for i in range(0,10):
#     l2.insertFront(i);
# print "The LinkedList should be [9,8,7,6,5,4,3,2,1,0]: " + str(l2.printList())
# print "Attempting remove node '6'"
# l2.remove(6)
# print "Now the LinkedList should be [9,8,7,5,4,3,2,1,0]: " + str(l2.printList())
#
# l3 = DList()
# print "Now the LinkedList should be empty and the function isEmpty should return True"
# print l3.isEmpty() and "True" or False
# l3.insertFront(333)
# print "Now the LinkedList should not be empty and the function isEmpty should return False"
# print l3.isEmpty() and "True" or False
# l3.remove(333)
# print "Now the LinkedList should be empty after removing node and the function isEmpty should return True"
# print l3.isEmpty() and "True" or False