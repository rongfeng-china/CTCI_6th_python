from LinkedList import *

########################
# partition, O(n)
########################

def partition(ll,p):
    if ll.head == None:
        return
    if ll.head.next == None:
        return
    p1 = ll.head
    p2 = ll.head.next
    while p2 != None:
        if p2.value < p:
            p1.next = p2.next
            p2.next = ll.head
            ll.head = p2
            p2 = p1.next
        else:
            p1 = p1.next
            p2 = p2.next

L1 = randomLinkedList(9,1,10)
print L1
partition(L1,5)
print L1
