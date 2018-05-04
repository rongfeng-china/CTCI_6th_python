from LinkedList import *

############################
#  sum list, reverse order
############################
def addLists(ll1,ll2):
    if ll1.head == None or ll2.head == None:
        print 'empty'
        return False
    v1, v2, a = 0,0,0
    cur1,cur2 = ll1.head, ll2.head
    L3 = LinkedList()
    while cur1 != None or cur2 != None:
        v1,v2 = 0,0
        if cur1!= None:
            v1 = cur1.value
            cur1 = cur1.next
        if cur2!= None:
            v2 = cur2.value
            cur2 = cur2.next
        v3 = v1+v2+a
        a,b = v3/10,v3%10
        L3.addNode(b)
    return L3
        
##############################
# sum list, forward order
#############################
def addLists2(ll1,ll2):
    if ll1.head == None or ll2.head == None:
        print 'empty'
        return False
    v1,v2 = 0,0
    cur1,cur2 = ll1.head,ll2.head
    L4 = LinkedList()
    while cur1 != None:
        v1 = v1*10 + cur1.value 
        cur1 = cur1.next
    while cur2 != None:
        v2 = v2*10 + cur2.value 
        cur2 = cur2.next
    v3 = str(v1+v2)
    for i in range(len(v3)):
        L4.addNode(v3[i])
    return L4

L1 = randomLinkedList(3,0,9)
L2 = randomLinkedList(3,0,9)
print L1
print L2
L3 = addLists(L1,L2)
if L3 is not False:
    print L3
L4 = addLists2(L1,L2)
if L4 is not False:
    print L4
