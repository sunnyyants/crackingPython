__author__ = 'SunnyYan'

# An animal shelter holds only dogs and cats, and operates
# on a strictly "first in, first out" basis. People must
# adopt either the "oldest" (based on arrival time) of all
# animals at the shelter, or they can select whether they
# would prefer a dog or a cat (and will receive the oldest
# animal of that type). They cannot select which specific
# animal they would like. Create the data structures to
# maintain this system and implement operations such as
# enqueue, dequeueAny, dequeueDog and dequeueCat.
# You may use the built-in LinkedList data structure.
import Linked_List

import Linked_List.DoubleLinkedList
from Linked_List.DoubleLinkedList import DList

class Animal:
    def __init__(self, name, type):
        self.timeStamp = 0
        self.name = name
        self.type = type

    def setTimeStamp(self, timeStamp):
        self.timeStamp = timeStamp

    def getTimeStamp(self):
        return self.timeStamp

    def isOlder(self,animal):
        return self.getTimeStamp() < animal.getTimeStamp()

    def getType(self):
        return (str)(self.type)

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name,"Dog")



class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self,name,"Cat")


class AnimalQueue:

    def __init__(self):
        self.dogs = DList()
        self.cats = DList()
        self.timeStamp = 0
        self.size = 0

    def enqueue(self,animal):
        animal.setTimeStamp(self.timeStamp)
        self.timeStamp += 1
        if(animal.getType() == "Dog"):
            self.dogs.insertBack(animal)
        elif(animal.getType() == "Cat"):
            self.cats.insertBack(animal)
        self.size += 1

    def dequeueCat(self):
        self.size -= 1
        return self.cats.poll().item

    def dequeueDog(self):
        self.size -= 1
        return self.dogs.poll().item

    def dequeueAny(self):
        if(self.dogs.size == 0):
            return self.dequeueCat()
        if(self.cats.size == 0):
            return self.dequeueDog()

        dog = self.dogs.getFront().item
        cat = self.cats.getFront().item

        if(dog.isOlder(cat)):
            return self.dequeueDog()
        else:
            return self.dequeueCat()

# Testing Parts..

DOGS = ["D1","D2","D3","D4","D5","D6"]
CATS = ["C1","C2","C3","C4","C5","C6"]

aq = AnimalQueue()
for i in range(0,len(DOGS)):
    dog = Dog(DOGS[i])
    cat = Cat(CATS[i])
    aq.enqueue(dog)
    aq.enqueue(cat)

print "The first dequeue animal should be dog D1: " + (str)(aq.dequeueAny().name)
print "Next dequeue animal should be cat C1: " + (str)(aq.dequeueAny().name)
print "Then hould be dog D2: " + (str)(aq.dequeueAny().name)
print "------------------------------------------------"
print "We now continuously dequeue 3 dogs, they should be D3 D4 D5: " + (str)(aq.dequeueDog().name) + ' ' \
      +  (str)(aq.dequeueDog().name) + ' ' + (str)(aq.dequeueDog().name)
print "------------------------------------------------"
print "We now continuously dequeue 2 cats, they should be C2 C3: "+ (str)(aq.dequeueCat().name) +' ' \
      + (str)(aq.dequeueCat().name)
print "------------------------------------------------"
print "We now enqueue D7 C7 C8 D8..."
dog1 = Dog("D7")
dog2 = Dog("D8")
cat1 = Cat("C7")
cat2 = Cat("C8")
animallist = [dog1,cat1,cat2,dog2]
for i in animallist:
    aq.enqueue(i)

print "After enqueued animals we dequeue all the rest animals.."
print "------------------------------------------------"
print "They should be C4 C5 D6 C6 D7 C7 C8 D8: ",
while(aq.size != 0):
    print (str)(aq.dequeueAny().name) + "",