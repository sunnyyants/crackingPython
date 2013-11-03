__author__ = 'SunnyYan'

# Describe how you could use a single array to implement
# three stacks

class arrayStacks:

    def __init__(self, stackNumber):
        self.stackSize = 300;
        self.stacknum = stackNumber
        self.array = [None] * self.stacknum * self.stackSize
        self.stacks = [0] * self.stacknum

    def isFull(self, stacknum):
        if(self.array[(stacknum - 1) *100] == None):
            return False
        else:
            return True

    def isEmpty(self, statcknum):
        if(self.array[statcknum] - 1 == None):
            return True
        else: return False

    def indexComputation(self, stacknum):
        index = 0
        switch()
    def push(self, stacknum, item):
        if(isFull(stacknum) == False):
            index = indexComputation(stacknum)
            self.array[index] = item
            self.stacks[stacknum - 1] += 1
        else:
            print "This stack is full!"

