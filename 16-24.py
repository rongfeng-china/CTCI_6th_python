def pairs_with_sum(arr,sum_value):
    arr = sorted(arr)
    result = []
    for index in range(len(arr)):
        num = arr[index]
        if num > sum_value/2:
            break
        brr = arr[0:index]
        if index < len(arr)-1:
            brr += arr[index+1:]
        re = binary_search(brr,sum_value-num,0,len(brr))
 
        if re != -1:
            result.append((num,sum_value-num))
    return result



def binary_search(arr,v,start,end):
    if start > end:
        return -1
    mid = (start+end)/2
    if arr[mid] == v:
        return mid
    elif arr[mid] < v:
        start = mid+1
    else:
        end = mid-1
    
    return binary_search(arr,v,start,end)
       

arr = [2, 3, 4, 11, -4]
result = pairs_with_sum(arr,7)
print result

arr = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 10, 20, 30, -11]
result = pairs_with_sum(arr,55)
print result
