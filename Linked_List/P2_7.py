__author__ = 'SunnyYan'

# Implement a function to check if a linked list is a palindrome

from Linked_List.SingleLinkedList import SLinkedList

def checkpalindrome(list):
    length = list.size
    findhalf = list.head
    reverse = SLinkedList()
    for i in range(0,length / 2):
        reverse.insertFront(findhalf.item)
        findhalf = findhalf.next
        if(i + 1 == length / 2 and length % 2 == 1):
            reverse.insertFront(findhalf.item)


    iter = reverse.head
    while(iter != None or findhalf != None):
        if(iter.item != findhalf.item):
            return False
        iter = iter.next
        findhalf = findhalf.next
    return True


#Testing Part...

T7 = SLinkedList()
T8 = SLinkedList()
l1 = [1,2,3,2,1]
l2 = [1,2,3,4,5,6,6,5,4,3,3,1]

for i in l1:
    T7.insertFront(i)

for j in l2:
    T8.insertFront(j)

print (str)(T7.printList()) + " is palindrome: " + (checkpalindrome(T7) and "True" or "False")
print (str)(T8.printList()) + " is palindrome: " + (checkpalindrome(T8) and "True" or "False")

