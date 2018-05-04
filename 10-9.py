def search(mat,r,c,s_i,e_i,v):
    result = []
    x,y = int((s_i[0]+e_i[0])/2),int((s_i[1]+e_i[1])/2)
    if x < 0 or x >= r or y < 0 or y >= c or s_i[0] > e_i[0] or s_i[1] > e_i[1]:
        return [[-1,-1]]
    if mat[x][y] < v:
        result1 = search(mat,r,c,[s_i[0],y+1],[x,e_i[1]],v)
        result2 = search(mat,r,c,[x+1,s_i[1]],e_i,v)
        if result1 != [[-1,-1]]:
            result += result1
        if result2 != [[-1,-1]]:
            result += result2
    elif mat[x][y] > v:
        result1 = search(mat,r,c,s_i,[x-1,e_i[1]],v)
        result2 = search(mat,r,c,[x,s_i[1]],[e_i[0],y-1],v)
        if result1 != [[-1,-1]]:
            result += result1
        if result2 != [[-1,-1]]:
            result += result2
    else:
        result1 = search(mat,r,c,[s_i[0],y+1],[x-1,e_i[1]],v)
        result2 = search(mat,r,c,[x+1,s_i[1]],[e_i[0],y-1],v)
        if result1 != [[-1,-1]]:
            result += result1
        if result2 != [[-1,-1]]:
            result += result2
        result += [[x,y]]
    return result


mat = [[1,   2,  3,  4,  5,  6,  7,  8,  9],
           [5,  10, 15, 20, 25, 30, 35, 40, 45],
           [10, 20, 30, 40, 50, 60, 70, 80, 90],
           [13, 23, 33, 43, 53, 63, 73, 83, 93],
           [14, 24, 34, 44, 54, 64, 74, 84, 94],
           [15, 25, 35, 45, 55, 65, 75, 85, 95],
           [16, 26, 36, 46, 56, 66, 77, 88, 99]]

result = search(mat,len(mat),len(mat[0]),[0,0],[len(mat)-1,len(mat[0])-1],10)
print result
result = search(mat,len(mat),len(mat[0]),[0,0],[len(mat)-1,len(mat[0])-1],56)
print result
result = search(mat,len(mat),len(mat[0]),[0,0],[len(mat)-1,len(mat[0])-1],99)
print result
