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

    def getSize(self):
        return self.size
    
class MyQueue:
    def __init__(self):
        self.s1 = SingleStack()
        self.s2 = SingleStack()
 
    def push(self,value):
        self.s1.push(value)

    def pop(self):
        for i in range(self.s1.getSize()):
            data = self.s1.pop()
            self.s2.push(data)
        value = self.s2.pop()
        for i in range(self.s2.getSize()):
            data = self.s2.pop()
            self.s1.push(data)
        return value

if __name__ == "__main__":
    mq = MyQueue()
    for i in range(25):
        mq.push(i)
    for i in range(26):
        print mq.pop()
    
