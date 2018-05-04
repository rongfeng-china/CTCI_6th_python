from LinkedList import *

class AnimalQueue:
    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()

    def enqueue(self,value):
        if len(value) != 2:
            print 'error'
        type, name = value[0],value[1]
        if type == 'cat':
            self.cats.addNode(value[1])
        elif type == 'dog':
            self.dogs.addNode(value[1])
        else:
            print 'type wrong'

    def dequeueAny(self):

    def dequeueDog(self):
        if self.dogs.getSize() <= 0:
            return 'no dogs'
        else:
            dog_name = dogs.removeFirst()
    def
    
aq = AnimalQueue()
aq.enqueue([cat,kate])
aq.enqueue([cat,jasica])
aq.enqueue([dog,jim])
aq.enqueue([dog,peter])
aq.enqueue([dog,jason])
aq.enqueue([cat,sarah])
aq.enqueue([cat,maren])





