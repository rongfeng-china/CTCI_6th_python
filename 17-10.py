def majority(arr):
    frequency = 0
    result = None
    for i in arr:
        if result == None:
            result = i
            frequency = 1
        else:
            if result == i:
                frequency += 1
            else:
                frequency -= 1
                if frequency == 0:
                    result = i
                    frequency = 1
    return result

arr = [1,2,5,9,5,9,5,5,5]
result = majority(arr)
print result

result = majority([1,3,9,3,9])
print result 

result = majority([4,4,4,4,1,2,3])
print result
