def searchRotatedArray(start_i,end_i,arr,v):
    mid_i = int((start_i+end_i)/2)
    result = -1
    if v > arr[mid_i]:
        if v > arr[end_i]:
            result = searchRotatedArray(start_i,mid_i-1,arr,v)
        else:
            result = searchRotatedArray(mid_i+1,end_i,arr,v)
    elif v < arr[mid_i]:
        if v < arr[start_i]:
            result = searchRotatedArray(mid_i+1,end_i,arr,v)
        else:
            result = searchRotatedArray(start_i,mid_i-1,arr,v)
    else:
        result = mid_i
    return result
    


arr = [15,16,19,20,25,1,3,4,5,7,10,14]
result = searchRotatedArray(0,len(arr)-1,arr,5)
print result
