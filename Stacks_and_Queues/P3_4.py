__author__ = 'SunnyYan'

# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different
# sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending
# order of size from top to bottom (i.e., each disk sits on top of an even larger one).
# You have the following constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto the next tower.
# (3) A disk can only be placed on top of a larger disk.
# Write a program to move the disks from the first tower to the last using stacks.

from Stack import Stack
class Tower:

    def __init__(self,i):
        self.stack = Stack()
        self.index = i

    def findex(self):
        return self.index

    def add(self, digit):
        self.stack.push(digit)

    def moveTopTo(self, T):
        top = self.stack.pop()
        #print top
        T.add(top)
        print "Move disk top " + (str)(top) + " from " + (str)(self.findex()) + " to " + (str)(T.findex())

    def moveDisks(self, n, destination, buffer):
        if(n > 0):
            self.moveDisks(n-1,buffer,destination)
            self.moveTopTo(destination)
            buffer.moveDisks(n-1,destination,self)

# Testing part...

Towers = [Tower(0),Tower(1),Tower(2)]
for i in range(2,-1,-1):
    Towers[0].add(i)

Towers[0].moveDisks(3,Towers[2],Towers[1])