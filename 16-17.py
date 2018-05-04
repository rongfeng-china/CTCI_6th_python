def c_sequence(arr):
    sum_dict = {}
    i = 0
    while i < len(arr):
        if arr[i] > 0:
            tmp = arr[i]
            for j in range(i+1,len(arr)):
                 if arr[j] > 0 or tmp + arr[j] > 0:
                    tmp += arr[j]
                    sum_dict[i,j] = tmp
                 else:
                     i = j
                     break
        i= i+1
    if sum_dict == {}:
        print max(arr)
        return

    sum_dict = sorted(sum_dict.iteritems(), key = lambda x:x[1])
    #print sum_dict
    start_index = sum_dict[-1][0][0]
    end_index = sum_dict[-1][0][1]
    sum_v = sum_dict[-1][1]
    print 'sequence is:'
    for i in range(start_index, end_index+1):
        print arr[i],
    print 'sum is %d' %(sum_v)
    return 

seq = [-1, 4, 4, -7, 8, 2, -4, 3]
c_sequence(seq)
seq = [-1, 4, 4, -7, 8, 2, -4, -3, 9]
c_sequence(seq)
seq = [-1, -4, -54, -7, -8, 2, -4, -3, 9]
c_sequence(seq)
seq = [-1, -4, -54, -7, -8, -2, -4, -3, -9]
c_sequence(seq)
