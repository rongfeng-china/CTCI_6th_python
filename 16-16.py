def sub_sort(arr):
    n = len(arr)
    left_index, right_index = -1,n-1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            left_index = i
            break
    if left_index == -1:
        print 'good'
        return 0

    for i in range(n-1,0,-1):
        if arr[i] < arr[i-1]:
            right_index = i
            break
    left = arr[0:left_index+1]
    mid = arr[left_index+1:right_index]
    right = arr[right_index:]

    min_v, max_v = 1000,-1000
    if mid == []:
        mid.append(arr[left_index])
        left = arr[0:left_index]
        left_index -= 1
    
    min_v,max_v = min(mid),max(mid)      

    end = left[-1] > min_v or right[0] < max_v
    while end:
        end = 0
        n_left,n_right = len(left),len(right)
        l1,l2 = -1,-1
        for index in range(n_left-1,-1,-1):
            if left[index] > min_v:
                l1 = index
            else:
                break
        if l1 != -1:
            if left[-1]>max_v:
                max_v = left[-1]
            left = left[:l1]
            
        for index in range(0,n_right):
            if right[index] < max_v:
                l2 = index
            else:
                break
        if l2 != -1:
            if right[0] < min_v:
                min_v = right[0]
            right = right[l2+1:]
         
        if left != []:
            if left[-1] > min_v:
                end = 1
        if right != []:
            if right[0] < max_v:
                end = 1
    print '%d %d' %(len(left),n-1-len(right))
    return  

array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
sub_sort(array)


array = [10, 11, 12, 13, 14, 16, 15, 17, 18, 19]
sub_sort(array)   

array = [10, 18, 12, 13, 14, 16, 15, 17, 11, 19]
sub_sort(array)
array = [90, 80, 70, 60, 50, 40, 30, 20, 10, 01]
sub_sort(array)                
                
                
            

