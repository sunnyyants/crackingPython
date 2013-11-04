__author__ = 'SunnyYan'

# Write a program to sort a stack in ascending order (with biggest items on top).
# You may use at most one additional stack to hold items, but you may not copy the
# elements into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and isEmpty.

from Stack import Stack

def sortStack(stacks):
    buffer = Stack()
    while(stacks.size !=0):
        temp = stacks.pop()
        while(buffer.size !=0 and temp < buffer.peek()):
            stacks.push(buffer.pop())
        buffer.push(temp)

    return buffer

# Testing part...

S6 = Stack()
for i in range(3,10):
    S6.push(i)
for i in range(0,4):
    S6.push(i)

print "The stack now is: " + S6.printStack()
print "After sorting.........."
result = sortStack(S6)

print "Now the stack becomes: " + result.printStack()
print "Checking the top should be the largest number of the stack: " +(str)(result.pop())
