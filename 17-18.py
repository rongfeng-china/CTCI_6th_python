def shortestSuperSequence(sA,bA):
    dict1 = {}
    for i in range(len(bA)):
        num = bA[i]
        if num in sA:
            if num in dict1:
                tmp_list = dict1[num]
                tmp_list.append(i)
                dict1[num] = tmp_list
            else:
                dict1[num] = [i]
    # print dict1
    re = cal(dict1,sA,[],0)
    min_v,max_v = re[0][0],re[0][1]
    result = max_v-min_v+1
    for i,j in re:
        if j-i+1 < result:
            result = j-i+1
            min_v,max_v = i,j
    return result,[min_v,max_v]

def cal(dict1,sA,pre_result,index):
    if index == 0:
        result = []
        v = sA[0]
        list1 = dict1[v]
        for num in list1:
            result.append([num,num])
        result = cal(dict1,sA,result,1)
    else:
        result = []
        for i in range(len(pre_result)):
            min_v, max_v = pre_result[i]
            num = sA[index]
            tmp_l = dict1[num]
            index1,index2 = len(tmp_l)-1,len(tmp_l)-1
            for i in range(len(tmp_l)-1):
                if tmp_l[i] <= min_v and tmp_l[i+1] >= min_v:
                    index1 = i
                    break
            for i in range(len(tmp_l)-1):
                if tmp_l[i] <= max_v and tmp_l[i+1] >= max_v:
                    index2 = i
                    break
            if index1 == index2:
                v1 = tmp_l[index1]
                result.append([v1,max_v])
                if index1 != len(tmp_l)-1:
                    v2 = tmp_l[index1+1]
                    result.append([min_v,v2])                   
            else:
                result.append([min_v,max_v])
        if index == len(sA)-1:
            return result
        else:
            result = cal(dict1,sA,result,index+1)
    return result

smallArray = [1, 5, 9]
bigArray = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
r1,r2 = shortestSuperSequence(smallArray,bigArray)
print r1,r2
