import math
def findMissing(arr,n,digits):
    result = ''
    for index in range(digits):
        count0,count1 = 0,0
        for num in arr:
            if int(num[digits-1-index]) == 0:
                count0 += 1
            else:
                count1 += 1
        if count0 <= count1:
            result+='0'
            arr = remove_v(arr,digits-1-index,1)
        else:
            result+='1'
            arr = remove_v(arr,digits-1-index,0)
        if len(arr) == 1:
            break
    print (digits-len(result))*'0'+result[::-1]
    

def remove_v(arr,index,v):
    for i in arr:
        if int(i[index]) == v:
            arr.remove(i)
    return arr

n = 10
remove_n = 5
digits = int(math.ceil(math.log(n-1,2)))
arr = [bin(i)[2:].zfill(digits) for i in range (n)]
arr.remove(bin(remove_n)[2:].zfill(digits))
findMissing(arr,n,digits)
