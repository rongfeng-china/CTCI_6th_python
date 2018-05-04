import copy
def getMaxBlackSquare(arr):
    m,n = len(arr),len(arr[0])
    left = copy.copy(arr)
    up  = copy.copy(arr)

    for i in range(1,m):
        for j in range(1,n):
            if arr[i][j] == 0:
                continue
            else:
                left[i][j] = left[i][j-1] + 1
        if arr[i][j] == 0:
            continue
        else:
            up[i][j] = up[i-1][j] + 1

    result = 0
    
    for i in range(m):
        for j in range(n):
            squareNum = getBiggestSquare(arr,i,j,left,up)
            if squareNum > result:
                result = squareNum
    return result     

def getBiggestSquare(arr,i,j,left,up):
    if arr[i][j] == 0:
        return 0
    dist = min(left[i][j],up[i][j])
    num = 0
    for k in range(dist-1,-1,-1):
        u,v = i-k,j-k
        if left[i][j]-left[u][v] >= k and up[i][j] - up[u][v] >= k:
            num = k
            break
    return num+1


arr = [[0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0]]
print getMaxBlackSquare(arr)

arr  = [[0, 0, 0], [0, 0, 0]]
print getMaxBlackSquare(arr)

arr = [[0, 1], [1, 0]]
print getMaxBlackSquare(arr)

arr = [[1, 1, 0], [1, 1, 0]]
print getMaxBlackSquare(arr)
