from LinkedList import *

def findBeginning(L1):
    slow,fast = L1.head, L1.head
    count = 0
    while (count == 0 or slow != fast) and fast != None:
        slow = slow.next
        fast = fast.next.next    
        count += 1
    slow = L1.head
    count = 0
    while slow != fast :
        slow = slow.next
        fast = fast.next
        count += 1
    return count+1

L1 = LinkedList()
L1.addNode(0)
L1.addNode(1)
L1.addNode(2)
L1.addNode(3)

L2 = LinkedList()
L2.addNode(4)
L2.addNode(5)
L2.addNode(6)
L2.addNode(7)
L2.addNode(8)
L2.addNode(9)

L1.tail.next = L2.head
L2.tail.next = L2.head

#print L1.head.next.next.next.next.next.next.value
print 'circule starts at Nth node, N = '+ str(findBeginning(L1))
