from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def addNode(self,value):
        node = Node(value)
        #if the old list is none, set new node as the first node
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        
    def __str__(self):
        if self.head != None:
            index = self.head
            nodestore = [str(index.value)]
            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))
            return "LinkedList  [ " + "->".join(nodestore) + " ]"
        return "LinkedList  []"

    def getSize(self):
        return self.size
        
    #remove the first node that have the same value as the given node_value
    def removeNode(self, node_value):
        current = self.head
        if current.value == node_value:
            self.head = self.head.next
        while(current.next != None):
            if current.next.value == node_value:
                current.next = current.next.next
                break
            else:
                current = current.next
        self.size -= 1

    def removeFirst(self):
        current = self.head
        if current == None:
            return None
        else:
            self.head= current.next
            return current.value

    def getFirst(self):
        return self.head.value
        
def randomLinkedList(length, min, max):
    linkedlist = LinkedList()
    for i in range(length):
        value = randint(min, max)
        linkedlist.addNode(value)
    return linkedlist



