class Box:
    def __init__(self,h,w,d):
        self.h = h
        self.w = w
        self.d = d

def boxStacks(index,pre_index,history,boxes,result):
    #print '%d %d' %(index,pre_index)
    #print history
    #print result
    if check(index,pre_index,boxes) or pre_index == -1:
        updated_history = history[:]
        updated_history[index] = 1
        result += boxes[index].h
        sub_result = []
        for i in range(len(updated_history)):
            if updated_history[i] == 0:
                re = boxStacks(i,index,updated_history,boxes,result)
                sub_result.append(re)
        if max(sub_result) == 0:
            print 'zero'
        result = max(sub_result)
    
    return result        


def check(index,pre_index,boxes):
    if boxes[index].h < boxes[pre_index].h and boxes[index].w < boxes[pre_index].w and boxes[index].d < boxes[pre_index].d:
        return True
    return False




box1 = Box(100,100,100)
box2 = Box(25,25,25)
box3 = Box(20,5,30)
box4 = Box(17,4,28)
boxes = [box1,box2,box3,box4]

print boxStacks(0,-1,[0,0,0,0],boxes,0)
