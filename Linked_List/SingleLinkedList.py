__author__ = 'SunnyYan'

class SNode:

    def __init__(self,item,next):
        self.item = item
        self.next = next


class SLinkedList:

    def __init__(self):
        self.size = 0;
        self.head = None
        self.tail = None

    def insertFront(self, item):
        self.head = SNode(item, self.head)
        if(self.isEmpty()):
            self.tail = self.head
        self.size += 1

    def insertBack(self, item):
        if (self.tail is None):
            self.tail = SNode(item, None)
            self.head = self.tail
        else:
            self.tail.next = SNode(item, None)
            self.tail = self.tail.next
        self.size += 1

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def isEmpty(self):
        return self.size is 0

    def remove(self,item):
        currentNode = self.head
        while(currentNode != None):
            if(currentNode.item is item):
                self.head = currentNode.next
            elif(currentNode.next.item is item):
                if(currentNode.next is self.tail):
                    self.tail = currentNode
                currentNode.next = currentNode.next.next
            currentNode = currentNode.next

    def printList(self):
        self.List = []
        currentNode = self.head
        while(currentNode != None):
            self.List.append(currentNode.item)
            currentNode = currentNode.next
        return self.List


# Testing single linked list
# l1 = SLinkedList()
# for i in range(0,10):
#     l1.insertBack(i)
#
# print "The Single LinkedList should be [0,1,2,3,4,5,6,7,8,9]: " +str(l1.printList())
#
# l2 = SLinkedList()
# for i in range(0,10):
#     l2.insertFront(i)
#
# print "The Single LinkedList should be [9,8,7,6,5,4,3,2,1,0]: " +str(l2.printList())
#
# print "The head of l1 now should be 0: " + str(l1.getHead().item)
# print "The tail of l1 now should be 9: " + str(l1.getTail().item)
# print "The head of l2 now should be 9: " + str(l2.getHead().item)
# print "The tail of l2 now should be 0: " + str(l2.getTail().item)
# print "Attempting remove node 9 from l1..."
# l1.remove(9)
# print "The Single LinkedList should be [0,1,2,3,4,5,6,7,8]: " +str(l1.printList())
# print "The tail of l1 now should be 8: " + str(l1.getTail().item)






