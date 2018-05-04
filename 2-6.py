from LinkedList import *

def isPalindrome(L1):
    L2 = reverseL(L1)
    print isEqual(L1,L2)

def reverseL(L1):
    L2 = LinkedList()
    node = L1.head
    while node != None:
        n = Node(node.value)
        n.next = L2.head
        L2.head = n
        node = node.next
    print 'reverse:'
    print L2
    return L2
    
def isEqual(L1,L2):
    h1, h2 = L1.head, L2.head
    while h1 is not None and h2 is not None:
        if h1.value != h2.value:
            return False
        h1 = h1.next
        h2 = h2.next
    return True
         
L1 = randomLinkedList(9,2,7)
print L1
isPalindrome(L1)

L2 = LinkedList()
L2.addNode(0)
L2.addNode(1)
L2.addNode(2)
L2.addNode(1)
L2.addNode(0)
print L2
isPalindrome(L2)
