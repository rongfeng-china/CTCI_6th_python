from LinkedList import *

# use hash table, O(n)
def deleteDups(linkedList):
    my_dict = {}
    my_ll = LinkedList()
    current  = linkedList.head
    while current.next != None:
        if current.value not in my_dict:
            my_ll.addNode(current.value) 
            my_dict[current.value] = 1
        current = current.next
    return my_ll

# no data structure, O(n2)
def deleteDups2(linkedList):
    current = linkedList.head
    while current != None:
        runner = current
        while runner.next != None:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return linkedList


L1 = randomLinkedList(9,3,7)
print L1
print deleteDups(L1)
print deleteDups2(L1)



