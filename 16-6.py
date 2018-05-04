def smallest_diff(arr1,arr2):
    index1, index2 = 0 ,0
    result = 100000
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    l1, l2 = len(arr1), len(arr2)
    while index1 <= l1 or index2 <= l2:
        val = arr1[index1] - arr2[index2]
        if abs(val) < result:
            result = abs(val)
        if val < 0:
            index1 += 1
            if index1 == l1:
                break
        else:
            index2 += 1
            if index2 == l2:
                break
    return result
        
        
    
result  = smallest_diff([11, 22, 33, 44], [77, 2, 66, 50])
print result

result  = smallest_diff([11, 22, 33, 44], [77, 2, 34, 50])
print result

result  = smallest_diff([11, 77, 33, 44], [77, 2, 34, 50])
print result

result  = smallest_diff([10, 20, 30, 40, 50, 60, 70, 80, 90], [33,45,58,17])
print result
