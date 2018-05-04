from LinkedList import *

#################################
# delete middle node, O(n)
# example: a->b->c->d->e->f
#          a->b->d->e->f
#################################
def deleteNode(ll,node):
    if node == None or node.next == None:
        ll = LinkedList()
    else:
        newNode = node.next
        node.value = newNode.value
        node.next = node.next.next
    
L1 = randomLinkedList(9, 3, 7)
print L1
node = L1.head.next.next
deleteNode(L1,node)
print L1


