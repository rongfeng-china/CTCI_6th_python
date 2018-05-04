from LinkedList import *

def findIntersection(L1,L2):
    if L1.tail != L2.tail:
        #print L1.tail
        #print L2.tail
        return None,None
    
    h1,h2 = L1.head, L2.head
    c1,c2 = 0,0
    if L1.size >= L2.size:
        for i in range(L1.size-L2.size):
            h1 = h1.next
        c1 = L1.size-L2.size
    else:
        for i in range(L2.size-L1.size):
            h2 = h2.next
        c2 = L2.size-L1.size
    while h1 is not None:
        if h1.value != h2.value:
            c1 += 1
            c2 += 1
            h1 = h1.next
            h2 = h2.next
        else:
            return c1+1,c2+1
        
        
# create two intersected linkedlist L1 and L2
L_intersection = LinkedList()
L1,L2 = LinkedList(),LinkedList()
L1.addNode(3)
L1.addNode(1)
L1.addNode(5)
L1.addNode(9)
L2.addNode(4)
L2.addNode(6)
L_intersection.addNode(7)
L_intersection.addNode(2)
L_intersection.addNode(1)
L1.tail.next = L_intersection.head
L2.tail.next = L_intersection.head
L1.tail = L_intersection.tail
L2.tail = L_intersection.tail
print L1
print L2

p1,p2 = findIntersection(L1,L2)
print p1,p2
