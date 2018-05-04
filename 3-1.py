class SingleStack:
    def __init__(self, stacksize = 100, number = 3):
        self.stacksize = stacksize
        self.number  = number
        self.array = [None]*self.stacksize*self.number
        self.pointer = [-1]*self.number

    def push (self, stacknum, value):
        if self.pointer[stacknum]+1 >= self.stacksize:
            print 'out of space'
        else:
            self.pointer[stacknum] += 1
            self.array[self.stacksize*stacknum+self.pointer[stacknum]]= value

    def pop(self,stacknum):
        if self.pointer[stacknum] < 0:
            return 'nothing in the stack'
        else:
            data = self.array[self.stacksize*stacknum+self.pointer[stacknum]]
            self.array[self.stacksize*stacknum+self.pointer[stacknum]] = None
            self.pointer[stacknum] -= 1    
            return data
    
    def peek(self,stacknum):
        if self.pointer[stacknum] < 0:
            return 'empty'
        else:
            return self.array[self.stacksize*stacknum+self.pointer[stacknum]]

    def isEmpty(self,stacknum):
        return self.pointer[stacknum] == -1


if __name__ == "__main__":
    arr1 = SingleStack(10,3)
    arr1.push(2,11)
    arr1.push(2,111)
    arr1.push(1,22)
    print arr1.pop(0)
    print arr1.peek(1)
    print arr1.pop(1)
    print arr1.pop(2)
    print arr1.pop(2)
    print arr1.pop(2)
   
    
