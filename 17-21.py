def calVolume(h):
    arr = []
    index,max_n = -1,0
    for i,n in enumerate(h):
        if n != 0:
            arr.append([i,n])
            if n > max_n:
                max_n = n
                index += 1
    result = 0
    
    result = calLeft(arr[:index+1])+calRight(arr[index:])

    return result

def calLeft(brr):
    result = 0
    if len(brr) == 1:
        return 0
    else:
        count,second_n = -1,0
        for i in range(len(brr)-1):
             n = brr[i][1]
             if n > second_n:
                 second_n = n
                 count +=1
        
        index1,v1 = brr[count]
        index2,v2 = brr[-1]
        result1= (index2-index1-1)*min(v1,v2)
        result2 = sum(x[1] for x in brr[count+1:len(brr)-1])
        result1 = result1-result2
        if count == 0:
            return result1
        else:
            result = calLeft(brr[:count+1])+result1
    return result
        

def calRight(brr):
    result = 0
    if len(brr) == 1:
        return 0
    else:
        count,second_n = 0,0
        for i in range(1,len(brr)):
             n = brr[i][1]
             if n > second_n:
                 second_n = n
                 count +=1
        
        index1,v1 = brr[0]
        index2,v2 = brr[count]
        result1 = (index2-index1-1)*min(v1,v2)
        result2 = sum(x[1] for x in brr[1:count])
        result1 = result1 - result2
        if count == len(brr)-1:
            return result1
        else:
            result = result1 + calRight(brr[count:])
    return result




h = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
print calVolume(h)

