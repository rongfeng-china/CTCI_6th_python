def equalize_sum_with_swap(arr1,arr2):
    arr1,arr2 = sorted(arr1),sorted(arr2)
    sum1,sum2= sum(arr1),sum(arr2)
    diff = 1.0*(sum1-sum2)/2

    dict1 = {}
    for i in arr1:
        dict1[i-diff]=i
    for i in arr2:
        if i in dict1:
            return (dict1[i],i)
    return None

arr1 = [5, 5, 10]
arr2 = [4, 4, 8]
result = equalize_sum_with_swap(arr1, arr2)
print result

arr1 = [5, 5, 5]
arr2 = [6, 4, 6]
result = equalize_sum_with_swap(arr1, arr2)
print result

arr1 = [5, 5, 14]
arr2 = [7, 7, 8]
result = equalize_sum_with_swap(arr1,arr2)
print result

arr1 = [5, 5, 14]
arr2 = [4, 10, 8]
result = equalize_sum_with_swap(arr1,arr2)
print result
