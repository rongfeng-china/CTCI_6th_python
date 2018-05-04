class SingleStack:
    def __init__(self):
        self.array = []
        self.size = 0

    def push (self,  value):
        self.array.append(value)
        self.size += 1

    def pop(self):
        if len(self.array) <= 0:
            return 'nothing in the stack'
        else:
            self.size -= 1
            return self.array.pop()

    def peek(self):
        if self.getSize() == 0:
            return None
        return self.array[-1]

    def getSize(self):
        return self.size

    def printStacks(self):
        print self.array
    
class myStack:
    def __init__(self):
        self.s1 = SingleStack()

    def push(self,value):
        self.s1.push(value)

    def pop(self):
        self.s1.pop()

    def sortStack(self):
        s2 = SingleStack()
        while self.s1.getSize() > 0:
            #self.s1.printStacks()
            #s2.printStacks()
            data = self.s1.pop()
            count = 0
            while s2.peek()!= None:
                if s2.peek() < data:
                    v = s2.pop()
                    self.s1.push(v)
                    count += 1
                else:
                    break
            s2.push(data)
            for i in range(count):
                v = self.s1.pop()
                s2.push(v)
        return s2       
                    

if __name__ == "__main__":
    ms = myStack()
    ll = [2,5,0,8,6]
    for i in ll:
        ms.push(i)
    ll2 = ms.sortStack()
    while ll2.getSize() > 0:
        print ll2.pop()

    
