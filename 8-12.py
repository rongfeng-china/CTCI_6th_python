def eightQueens(n,r,history):
    if r >= n:
        return 1 
    old_set = set([0,1,2,3,4,5,6,7])
    new_set = set(processAll(history,r,n))
    diff = list(old_set-new_set)
    update_history = history[:]
    num = 0
    for i in range(len(diff)):
        update_history = history+[[r,diff[i]]] 
        v = eightQueens(n,r+1,update_history)
        num += v
    return num


def processAll(history,r,n):
    value = [] ## columns that are not available
    for item in history:
        results  = process(item,r,n)
        value+=results
    return value

def process(item,r,n):
    r0,c0 = item[0],item[1]
    v1 = r-r0+c0
    v2 = c0-(r-r0)
    v3 = c0
    lists = [v1,v2,v3]
    results = []
    for i in lists:
        if i >=0 and i < n:
            results.append(i)
    return results


print eightQueens(8,1,[[0,0]])+eightQueens(8,1,[[0,1]])+eightQueens(8,1,[[0,2]])+eightQueens(8,1,[[0,3]])+eightQueens(8,1,[[0,4]])+eightQueens(8,1,[[0,5]])+eightQueens(8,1,[[0,6]])++eightQueens(8,1,[[0,7]])

#print eightQueens(8,7,[[0,3],[1,1],[2,7],[3,4],[4,6],[5,0],[6,2]])
