def paintFill(arr,i,j,o,n):
    r,c = len(arr),len(arr[0])
    if i < 0 or i >= r or j < 0 or j >= c:
        return arr
    if arr[i][j] != o:
        return arr
    arr[i][j] = n
    arr = paintFill(arr,i-1,j,o,n)
    arr = paintFill(arr,i+1,j,o,n)
    arr = paintFill(arr,i,j-1,o,n)
    arr = paintFill(arr,i,j+1,o,n)
    return arr

def paintFillAll(arr,i,j,n):
    o = arr[i][j]
    return paintFill(arr,i,j,o,n)

image1 = [[10, 10, 10, 10, 10, 10, 10, 40],
              [30, 20, 20, 10, 10, 40, 40, 40],
              [10, 10, 20, 20, 10, 10, 10, 10],
              [10, 10, 30, 20, 20, 20, 20, 10],
              [40, 40, 10, 10, 10, 10, 10, 10]]

image2 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [10, 10, 20, 20, 30, 30, 30, 30],
              [10, 10, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]

image3 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [30, 30, 20, 20, 30, 30, 30, 30],
              [30, 30, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]


print paintFillAll(image1,1,3,30)
print image2

image1 = paintFillAll(image1,1,3,10)
print paintFillAll(image1,1,3,30)
print image3
