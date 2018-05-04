class SingleStack:
    def __init__(self, stacksize = 100, number = 3):
        self.stacksize = stacksize
        self.number  = number
        self.array = [None]*self.stacksize*self.number
        self.minarray = [None]*self.stacksize*self.number
        self.pointer = [-1]*self.number

    def push (self, stacknum, value):
        if self.pointer[stacknum]+1 >= self.stacksize:
            print 'out of space'
        else:
            self.pointer[stacknum] += 1
            self.array[self.stacksize*stacknum+self.pointer[stacknum]]= value
            if self.pointer[stacknum] == 0:
	        self.minarray[self.stacksize*stacknum+self.pointer[stacknum]] = value
            elif self.array[self.stacksize*stacknum+self.pointer[stacknum]] >= self.minarray[self.stacksize*stacknum+self.pointer[stacknum]-1]:
	        self.minarray[self.stacksize*stacknum+self.pointer[stacknum]] = self.minarray[self.stacksize*stacknum+self.pointer[stacknum]-1] 
            else:
                self.minarray[self.stacksize*stacknum+self.pointer[stacknum]]=value

    def pop(self,stacknum):
        if self.pointer[stacknum] < 0:
            return 'nothing in the stack'
        else:
            data = self.array[self.stacksize*stacknum+self.pointer[stacknum]]
            self.array[self.stacksize*stacknum+self.pointer[stacknum]] = None
            self.minarray[self.stacksize*stacknum+self.pointer[stacknum]]=None
            self.pointer[stacknum] -= 1    
            return data
    
    def peek(self,stacknum):
        if self.pointer[stacknum] < 0:
            return 'empty'
        else:
            return self.array[self.stacksize*stacknum+self.pointer[stacknum]]

    def isEmpty(self,stacknum):
        return self.pointer[stacknum] == -1

    def getMin(self,stacknum):
        return self.minarray[self.stacksize*stacknum+self.pointer[stacknum]]

if __name__ == "__main__":
    arr1 = SingleStack(20,3)
    arr1.push(0,5)
    print arr1.getMin(0)
    arr1.push(0,1)
    print arr1.getMin(0)
    arr1.push(0,2)
    arr1.push(0,0)
    arr1.push(0,4)
    
    print arr1.getMin(0)
 
    print 'start'
    arr1.pop(0)
    print arr1.getMin(0)
    arr1.pop(0)
    print arr1.getMin(0)
    arr1.pop(0)
    print arr1.getMin(0)
    arr1.pop(0)
    print arr1.getMin(0)
    arr1.pop(0)
    print arr1.getMin(0)
    
