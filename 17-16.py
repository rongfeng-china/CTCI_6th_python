def maxMinutes(arr):
    if len(arr) == 2 or len(arr) == 1:
        return max(arr)
    elif len(arr) == 3:
        return max(arr[0]+arr[2],arr[1])
    else:
        result = max(arr[0]+maxMinutes(arr[2:]),arr[1]+maxMinutes(arr[3:]))
    return result


arr = [30, 15, 60, 75, 45, 15, 15, 45]
print maxMinutes(arr)


arr = [75, 105, 120, 75, 90, 135]
print maxMinutes(arr)











