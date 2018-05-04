import random
def quicksort(arr,k):
    pivot = arr[-1]
    i,j = -1,0
    while j < len(arr):
        if arr[j] <= pivot: 
            i+= 1
            tmp = arr[i]
            arr[i]= arr[j]
            arr[j] = tmp
        j+= 1
    if i < k:
        result = arr[:i]+quicksort(arr[i:],k-i)
    elif i == k:
        result = arr[:i]
    else:
        result = quicksort(arr[:i],k)
    return result
            
arr = [10,50,30,80,90,70,20]
result = quicksort(arr,4)
print result

arr = [5, 1, 2, 10, 15, 23, 7, 3, 3, 7]
result = quicksort(arr,4)
print result

result = quicksort(arr,8)
print result

