def search(arr,s_i,e_i,v):
    result = -1
    index = int((s_i+e_i)/2)
    if arr[index] == "":
        index = ClosestLeftIndex(arr,s_i,index-1)
        if index == -1:
            index = ClosestRightIndex(arr,index+1,e_i)
    if arr[index] > v:
        result = search(arr,s_i,index-1,v)
    elif arr[index] < v:
        result = search(arr,index+1,e_i,v)
    else:
        result = index
    return result

def ClosestLeftIndex(arr,index1,index2):
    for i in range(index2,index1-1,-1):
        if (arr[i] != ""):
            return i
    return -1

def ClosestRightIndex(arr,index1,index2):
    for i in range(index1,index2+1):
        if (arr[i] == ""):
            return i
    return -1

arr = ["at","","","","ball","","","car","","","dad","",""]
result = search(arr,0,len(arr)-1,"ball")
print result
            
