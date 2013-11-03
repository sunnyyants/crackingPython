__author__ = 'SunnyYan'

# Implement a Queue data structure class

from Stack import Node

class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enQueue(self, item):
        if(self.first == None):
            self.first = Node(None,item);
            self.last = self.first
        else:
            self.last.setNext(Node(None,item))
            self.last = self.last.getNext()
        self.size += 1

    def deQueue(self):
        if(self.first != None):
            node = self.first
            self.first = self.first.getNext()
            self.size -= 1
            return node.item
        return None

    def isEmpty(self):
        return self.size == 0

    def qSize(self):
        return self.size

    def printQueue(self):
        node = self.first
        q = []
        while(node != None):
            q.append(node.item)
            node = node.next
        return (str)(q)

# Testing Part...
#
# q0 = Queue()
# for i in range(0,10):
#     q0.enQueue(i)
#
# print q0.qSize()
# print "Now the queue should be [0,1,2,3,4,5,6,7,8,9]: " + q0.printQueue()
#
# print "Now testing the dequeue function..."
# print "The first element is dequeued from queue should be 0: "+(str)(q0.deQueue())
# print "Then is 1: " + (str)(q0.deQueue())
# print "Now the queue becomes [2,3,4,5,6,7,8,9]: " + q0.printQueue()
