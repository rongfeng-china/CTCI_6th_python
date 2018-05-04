def makeChange(money,index,arr):
    if index == 3:
        arr_tmp = arr[:]
        arr_tmp[3] = money
        
        return [arr_tmp]

    coins = [25,10,5,1]
    cent = coins[index]
    v = money/cent
    result = []
    #print '%d %d' %(money,index)
    for i in range(v+1):
        arr_tmp = arr[:]
        m = money - i * cent
        arr_tmp[index] = i
        method = makeChange(m,index+1,arr_tmp)
        for item in method:
            result.append(item)
    return result


print makeChange(51,0,[0,0,0,0])


