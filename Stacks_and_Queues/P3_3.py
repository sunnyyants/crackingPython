__author__ = 'SunnyYan'


# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
# in real life, we would likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of
# several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
# (that is, pop() should return the same values as it would if there were just a single stack).
#
# FOLLOW UP
# Implement a function popAt(int index) which perform a pop operation on a specific sub-stack.

from Stack import Stack

class SetOfStacks:

    def __init__(self):
        self.stackPointer = 0
        #self.currentStacksize = 1
        #self.setTop = None
        self.LIMIT = 3
        self.currentStack = Stack()
        self.SOS = [self.currentStack]


    def push(self,item):
        if(self.currentStack.size >= self.LIMIT):
            #self.currentStacksize = 1
            self.stackPointer += 1
            #print self.stackPointer
            self.currentStack = Stack()
            self.SOS.append(self.currentStack)
        #print self.stackPointer
        self.currentStack.push(item)
        self.SOS[self.stackPointer] = self.currentStack

    def pop(self):
        self.currentStack = self.SOS[self.stackPointer]
        if(self.currentStack.size <= 0):
            self.stackPointer -= 1
            self.currentStack = self.SOS[self.stackPointer]

        return self.currentStack.pop()

    def popAt(self, index):
        self.currentStack = self.SOS[index - 1 ]
        if(self.currentStack.size <= 0):
            self.stackPointer -= 1
            self.currentStack = self.SOS[self.stackPointer]
        return self.currentStack.pop()

    def getSizeofSOS(self):
        return self.stackPointer + 1

    def getSizeofSubStack(self, index):
        self.currentStack = self.SOS[index - 1]
        return self.currentStack.size

# Testing Part

S3 = SetOfStacks()
for i in range(0,3):
    S3.push(i)
print "The item above are stored in stack 1: " + (str)(S3.getSizeofSOS())
print "The size of this stack should be 3: " + (str)(S3.getSizeofSubStack(S3.getSizeofSOS()))
print "-----------------------------------------------------------"
for i in range(3,6):
    S3.push(i)
print "The item above are stored in stack 2: " + (str)(S3.getSizeofSOS())
print "The size of this stack should be 3: " + (str)(S3.getSizeofSubStack(S3.getSizeofSOS()))
print "-----------------------------------------------------------"
for i in range(6,8):
    S3.push(i)
print "The item above are stored in stack 3: " + (str)(S3.getSizeofSOS())
print "The size of this stack should be 2: " + (str)(S3.getSizeofSubStack(S3.getSizeofSOS()))
print "-----------------------------------------------------------"
print "The first pop out element should be 7: " + (str)(S3.pop())
print "Now the sie of stack 3 should be 1: " + (str)(S3.getSizeofSubStack(S3.getSizeofSOS()))
print "-----------------------------------------------------------"
print "The first pop out element in stack 1 should be 2: " + (str)(S3.popAt(1))
#print "The first pop out element in stack 1 should be 1: " + (str)(S3.popAt(1))
print "The first pop out element in stack 2 should be 5: " + (str)(S3.popAt(2))
print "-----------------------------------------------------------"
print "Pop out all the rest elements in the set of stacks: "
print "They should be [6,4,3,1,0]..."
list = []
while(S3.getSizeofSubStack(1) != 0):
    list.append(S3.pop())

print list
