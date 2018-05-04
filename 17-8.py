def longestIncreasingSeq(circus,l1,l2,pre):
    result = []
    if pre == []:
        if l1[0]==l2[0]:
            result = longestIncreasingSeq(circus,l1,l2,[l1[0][0]])
        else:
            result = longestIncreasingSeq(circus,l1,l2,[[l1[0][0]],[l2[0][0]]])
    else:
        end = 1
        for index in range(len(pre)):
            pre_index = pre[index][-1]
            v1 =  [i for i in range(len(l1)) if l1[i][0] == pre_index][0]
            v2 =  [i for i in range(len(l2)) if l2[i][0] == pre_index][0]
            
            if v1 == (len(l1)-1) or v2 == (len(l2)-1) :
                pre[index].append(-1)
            else:
                tmp_index = -2
                for i in range(v1+1,len(circus)):
                    tmp_index =  l1[i][0]
                    if circus[tmp_index][1] < circus[pre_index][1]:
                        pre[index].append(tmp_index)
                        break
                for i in range(v2+1, len(circus)):
                    tmp_index2 = l2[i][0]
                    if circus[tmp_index2][0] < circus[pre_index][0]:
                        if tmp_index2 != tmp_index:
                            tmp = pre[index]
                            tmp.append(tmp_index2)
                            pre.append(tmp)
                            break
            for item in pre:
                if item[-1] != -1:
                    end = 0
            if end == 1:
                return pre
        for item in pre:
            if item[-1] != -1:
                end = 0
        if end == 1:
            return pre
        else:
            result = longestIncreasingSeq(circus,l1,l2,pre)
    return result
def sort_l1_l2(circus):
    l1 = sorted(circus.iteritems(), key = lambda x:x[1][0],reverse=True)
    l2 = sorted(circus.iteritems(), key = lambda x:x[1][1],reverse=True)
    return l1,l2
    
def len_final(tmp_result):
    result = 0
    max_arr = []
    for i in tmp_result:
        tmp = len(i)-1
        if tmp > result:
            result = tmp
            max_arr = i
    return result, max_arr[:-1]


circus = {0:[180,120],1:[170,140],2:[160,100],3:[155,170]}
l1,l2 = sort_l1_l2(circus)
tmp_result = longestIncreasingSeq(circus,l1,l2,[])
r1,r2 =len_final(tmp_result)
print r1
print r2
