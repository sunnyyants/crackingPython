__author__ = 'SunnyYan'

# How would you design a stack which, in addition to push and pop, also has a function min
# which returns the minimum element? Push, pop and min should all operate in O(1) time.

from Stack import Node

class BigOstack:

    def __init__(self):
        self.min = None
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        if self.isEmpty():
            self.top = Node(None, item)
            self.min = self.top
        else:
            node = Node(self.top, item)
            if item < self.min.item:
                newMin = Node(self.min, item)   # Construct a sub-linked list of minimum element
                self.min = newMin               # in the stack
            self.top = node
        self.size += 1

    def pop(self):
        if(self.isEmpty()):
            print "Stack is empty!"
        else:
            node = self.top
            if node.item == self.min.item:      # Update the min element in the stack
                self.min = self.min.next
            self.top = self.top.next
            self.size -= 1
            return node.item

    def findMin(self):
        return self.min.item

    def printStack(self):
        list = []
        currentNode = self.top
        while(currentNode != None):
            list.append(currentNode.item)
            currentNode = currentNode.next
        return (str)(list)


# Testing part...
S2 = BigOstack()
for i in range(1,7):
    S2.push(i)

for i in range(0,4):
    S2.push(i)

print "The Stack now is: " + S2.printStack()
print "The min element in stack should be 0: " + (str)(S2.findMin())
print "The first pop out element is 3: " + (str)(S2.pop())
S2.push(-4)
S2.push(-1)
print "The stack becomes: " + S2.printStack()
print "Now the minimum num in the stack should be -4: " + (str)(S2.findMin())
print "Now we pop the -1,-4,1,0 elements in the stack..."
for i in range(0,5):
    S2.pop()

print "Now the minimum num in the stack should be 1: " + (str)(S2.findMin())



