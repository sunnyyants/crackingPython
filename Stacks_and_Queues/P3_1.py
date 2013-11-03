__author__ = 'SunnyYan'

# Describe how you could use a single array to implement
# three stacks

class arrayStacks:

    def __init__(self, stackNumber):
        self.stackSize = 300;
        self.stacknum = stackNumber
        self.array = [None] * self.stacknum * self.stackSize
        self.stacks = [0] * self.stacknum
        self.dict = {'1':100, '2':200, '3':300}

    def isFull(self, stacknum):
        if(self.array[(stacknum - 1) *100] == None):
            return False
        else:
            return True

    def isEmpty(self, statcknum):

        if(self.array[self.dict[(str)(statcknum)] - 1] == None):
            return True
        else: return False

    def indexComputation(self, stacknum):
        dict = {'1':100 - self.stacks[0], '2':200 - self.stacks[1], '3':300 - self.stacks[2]};
        index = dict[str(stacknum)]
        return index

    def push(self, stacknum, item):
        if(self.isFull(stacknum) is False):
            index = self.indexComputation(stacknum)
            self.array[index - 1] = item
            self.stacks[stacknum - 1] += 1
        else:
            print "This stack is full!"

    def pop(self,stacknum):
        if(self.isEmpty(stacknum)):
            print "This stack is empty!"
        else:
            index = self.indexComputation(stacknum)
            result = self.array[index];
            self.array[index] = None
            self.stacks[stacknum-1] -= 1
            return result

    def size(self,stacknum):
        return self.stacks[stacknum - 1]

    def printStack(self, stacknum):
        list = []
        dict = {'1':100-self.stacks[0],'2':200-self.stacks[1],'3':300-self.stacks[2]}
        index = dict[(str)(stacknum)]
        for i in range(index, self.dict[(str)(stacknum)]):
            list.append(self.array[i])
        return (str)(list)


# Testing Part...

S1 = arrayStacks(3)
for i in range (0,10):
    S1.push(1,i)
for i in range (10,20):
    S1.push(2,i)
for i in range(30,40):
    S1.push(3,i)

print "Now the stack 1 should be [9,8,7,6,5,4,3,2,1,0]: " + S1.printStack(1)
print "The first element is pop out should be 9: " + (str)(S1.pop(1))
print "Now the stack 1 should be [8,7,6,5,4,3,2,1,0]: " + S1.printStack(1)
print "Checking the stack 2: " + S1.printStack(2)
S1.push(2,12345)
print "Now the stack becomes [12345,19,18,17,16,15,14,13,12,11,10]: " + S1.printStack(2)

print "Checking the stack 3: " + S1.printStack(3)
S1.pop(3)
S1.pop(3)
print "After poping 2 elements from stack 3 the stack 3 is now: " + S1.printStack(3)




