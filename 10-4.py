def searchNoSize(listy,left,index,right,v):
    result = -1
    if listy[index] == -1 or listy[index] > v:
        result = searchNoSize(listy,left,int((left+index)/2),right,v)
    elif listy[index] < v:
        result = searchNoSize(listy,index+1,int((index+right)/2),right,v)
    else:
        result = index
    return result

listy = [1,2,3,5,7,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, -1, -1, -1, -1]
result = searchNoSize(listy,0,18,18,18)
print result
