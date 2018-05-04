def ant(arr,steps,i,j,direction):
    m,n = len(arr),len(arr[0])
    dict = create(arr,m,n)
    for k in range(steps):
        if dict[i,j] == 'w':
            dict[i,j] = 'b'
            direction = new_direction('w',direction)
            i, j = move(i,j,direction)
        else:
            dict[i,j] = 'w'
            direction = new_direction('b',direction)
            i, j = move(i,j,direction)
    print i,j
    print_board(dict,m,n)

def print_board(dict,m,n):
    for i in range(m):
        for j in range(n):
            if dict[i,j] == 'w':
                print '0 ',
            else:
                print '1 ',
        print '\n'
def new_direction(color,direction):
    clockwise = {'r':'d','d':'l','l':'u','u':'r'}
    un_clockwise = {'r':'u','u':'l','l':'d','d':'r'}
    if color == 'w':
        return clockwise[direction]
    else:
        return un_clockwise[direction] 
        
def move(i,j,direction):
    if direction == 'r':
        return i,j+1
    elif direction == 'l':
        return i,j-1
    elif direction == 'u':
        return i-1,j
    else:
        return i+1,j

def create(arr,m,n):
    dict = {}
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                dict[i,j] = 'b'
            else:
                dict[i,j] = 'w'
    return dict


arr = [[1,0,1,1,0,1,0],[0,1,0,0,1,0,1],[1,1,1,0,1,1,0],[1,0,0,1,0,1,1],[0,1,1,0,1,0,1],[0,1,0,1,0,0,1]]
ant(arr,3,3,3,'r')

