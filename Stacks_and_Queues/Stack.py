__author__ = 'SunnyYan'

# Implement a Stack data structure class

class Node:

    def __init__(self, next, item):
        self.next = next
        self.item = item

    def getNext(self):
        return self.next

    def getItem(self):
        return self.item

    def setNext(self, next):
        self.next = next

    def setItem(self, item):
        self.item = item


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def pop(self):
        if(self.size > 0):
            node = self.top
            self.top = self.top.next
            self.size -= 1
            return node.item
        else: return None

    def push(self,item):
        node = Node(self.top,item)
        self.top = node
        self.size += 1

    def isEmpty(self):
        return self.size is 0

    def peek(self):
        return self.top.item

    def printStack(self):
        node = self.top
        s = []
        while(node != None):
            s.append(node.item)
            node = node.next
        return (str)(s)


# Testing Part...
#
# s0 = Stack()
# for i in range(0,10):
#     s0.push(i)
#
# print "Now the stack should be:[9,8,7,6,5,4,3,2,1,0]: " + s0.printStack()

# print "Now testing the pop function..."
# print "The first element which is pop out should be 9: " + (str)(s0.pop())
# print "Then is 8: " + (str)(s0.pop())
# print "Now the stack should be:[7,6,5,4,3,2,1,0]: "+ (str)(s0.printStack())