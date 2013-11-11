__author__ = 'SunnyYan'

# A child is running up a staircase with n steps, and can hop either 1 step,
# or 2 steps, or 3 steps at a time. Implement a method to count how many
# possible way the child can run up the stair.

def runningStair(n):
    if(n<0):
        return 0
    elif(n == 0):
        return 1
    return runningStair(n-1) + runningStair(n-2) + runningStair(n-3)


def runningStairDP(n, store):

    if(n < 0):
        return 0
    elif(n == 0):
        return 1
    elif(store[n] != 0):
        return store[n]
    else:
        store[n] = runningStairDP(n-1,store) + \
               runningStairDP(n-2,store) + \
               runningStairDP(n-3,store)
        return store[n]

# Testing Part...

list = [0] * 4
print runningStair(3)
print runningStairDP(3,list)