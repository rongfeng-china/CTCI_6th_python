def pond_sizes(arr):
    n,m = len(arr),len(arr[0])
    visited = [[False for i in range(m)] for j in range(n)]
    pond_list = []
    for i in range(n):
         for j in range(m):
             count = calculate(arr,visited,n,m,i,j)
             if count != 0:
                 #print i,j
                 #print count
                 pond_list.append(count)
    print pond_list

def calculate(arr,visited,n,m,seed_i,seed_j):
    if seed_i < 0 or seed_i >= n or seed_j < 0 or seed_j >= m:
        return 0
    elif visited[seed_i][seed_j]:
        return 0
    elif arr[seed_i][seed_j] != 0:
        visited[seed_i][seed_j] = True
        return 0
    else:
        visited[seed_i][seed_j] = True
        return 1 + calculate(arr,visited,n,m,seed_i-1,seed_j-1)+calculate(arr,visited,n,m,seed_i-1,seed_j)+calculate(arr,visited,n,m,seed_i-1,seed_j+1)+calculate(arr,visited,n,m,seed_i,seed_j-1)+calculate(arr,visited,n,m,seed_i,seed_j+1)+calculate(arr,visited,n,m,seed_i+1,seed_j-1)+calculate(arr,visited,n,m,seed_i+1,seed_j)+calculate(arr,visited,n,m,seed_i+1,seed_j+1)
        
        
    


terrain = [[0, 0, 1, 2, 3, 1, 1, 1],
           [1, 1, 1, 2, 2, 2, 0, 1],
           [1, 0, 1, 1, 2, 1, 1, 2],
           [0, 1, 0, 1, 3, 1, 2, 3]]
result = pond_sizes(terrain)

terrain = [[0, 0, 1, 2, 3, 1, 0, 1, 1],
               [0, 1, 1, 2, 2, 2, 0, 0, 1],
               [1, 0, 1, 0, 0, 1, 1, 0, 2],
               [0, 1, 1, 1, 0, 1, 2, 0, 2],
               [0, 1, 2, 1, 1, 1, 1, 0, 0]]

result = pond_sizes(terrain)
