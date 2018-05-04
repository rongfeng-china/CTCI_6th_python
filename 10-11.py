def peaks_and_valleys(arr):
    if len(arr) < 3:
        return 
    for i in range(len(arr)-1):
        if i % 2 == 1:
            if arr[i] < arr[i+1]:
                arr[i],arr[i+1]= arr[i+1],arr[i]
        else:
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    
a = [12, 6, 3, 1, 0, 14, 13, 20, 22, 10]
peaks_and_valleys(a)
print a
b = [34, 55, 60, 65, 70, 75, 85, 10, 5, 16]
peaks_and_valleys(b)
print b
