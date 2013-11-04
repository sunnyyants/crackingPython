__author__ = 'SunnyYan'

# Implement a MyQueue class which implements a queue using
# two stacks

from Stack import Stack

class MyQueue:

    def __init__(self):
        self.stack = Stack()
        self.buffer = Stack()
        self.size = 0


    def enqueue(self, item):
        self.buffer.push(item)
        self.size += 1

    def dequeue(self):
        while(self.buffer.size != 0):
            self.stack.push(self.buffer.pop())
        return self.stack.pop()

    def peek(self):
        while(self.buffer.size != 0):
            self.stack.push(self.buffer.pop())
        return self.stack.peek()

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def printQueue(self):
        return self.buffer.printStack()

# Testing part

Q1 = MyQueue()

for i in range(0,10):
    Q1.enqueue(i)

print "The queue is now: " + Q1.printQueue()
print "The first dequeue element should be 0: " + (str)(Q1.dequeue())
print "Next dequeue element should be 1: " +(str)(Q1.dequeue())
print "Then should be 2: " +(str)(Q1.dequeue())
print "Peek the top element on the queue, it should be 3: " + (str)(Q1.peek())


