class SetofStacks:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []

    def push (self,  value):
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([value])
        else:
            self.stacks[-1].append(value)

    def pop(self):
        if len(self.stacks) <= 0:
            return 'nothing in the stack'
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        data = self.stacks[-1].pop() 
        return data
    
    # Shift between sub-stacks can be considered, but not included here
    def popAt(self,index):
        if len(self.stacks[index]) ==0  or index < 0  or index > len(self.stacks):
            return 'empty stack'
        else:
            return self.stacks[index].pop()



if __name__ == "__main__":
    ss = SetofStacks(10)
    for i in range(25):
        ss.push(i)
    for i in range(3):
        print ss.pop()
    print ss.popAt(0)
    print ss.popAt(1)
    print ss.popAt(2)
    
