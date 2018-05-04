from LinkedList import *

# print from k the value, O(n)
def printKthToLast(ll,k):
    count = 1
    current = ll.head
    while current != None:
        if count >= k:
            print current.value
        count += 1
        current = current.next
        
L1 = randomLinkedList(0,3,7)
print L1
printKthToLast(L1,3)
