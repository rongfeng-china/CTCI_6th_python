def convert(arr):
    for i in range(len(arr)):
        if arr[i] >= 'a' and arr[i] < 'z':
            arr[i] = 'a'
        else:
            arr[i] = '1'
    return arr

def findLongestSubarray(arr):
    arr = convert(arr)
    count_diff = []
    count_a, count_1 = 0,0
    for i in arr:
        if i == 'a':
            count_a += 1
        else:
            count_1 += 1
        count_diff.append(count_a - count_1)
    my_dict = {}
    max_diff_v = 0
    index1,index2 = 0,len(arr)-1
    for index in range(len(count_diff)):
        item = count_diff[index]
        if item not in my_dict:
            my_dict[item] = [index,index]
        else:
            v1,v2 = my_dict[item]
            if index < v1:
                my_dict[item] = [index,v2]
                if v2-index > max_diff_v:
                    max_diff_v = v2-index
                    index1,index2 = index,v2
            if index > v2:
                my_dict[item] = [v1,index]
                if index-v1 > max_diff_v:
                    max_diff_v = index-v1
                    index1,index2 = v1,index
    print index1,index2                

arr = ['b','a','d','a','1','1','q','8','9','f','a','1','a','a','3','m','a','a','a','a']
findLongestSubarray(arr)
arr = ['a','1','a','a','a','1','1','1','a','1','a','a','1','1','a','a','a','a','a','a']
findLongestSubarray(arr)
