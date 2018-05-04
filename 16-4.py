def tic_tac_win(board):
    n = len(board)
    for i in range(n):
        count_o, count_x = 0,0
        for j in range(n):
            if board[i][j] == "o":
                count_o += 1
            else:
                if board[i][j] == "x":
                    count_x += 1
        if count_o == n:
            return 0 # o win
        else:
           if count_x == n:
               return 1  # x win
    for i in range(n):
        count_o,count_x = 0,0
        for j in range(n):
            if board[j][i] == "o":
                count_o += 1
            else:
                if board[j][i] == "x":
                    count_x += 1
        if count_o == n:
            return 0
        else:
            if count_x == n:
                return 1

    count_o,count_x = 0,0
    for i in range(n):
        if board[i][i] == "o":
            count_o += 1
        else:
            if board[i][i] == "x":
                count_x += 1
    if count_o == n:
        return 0
    else:
        if count_x == n:
            return 1

    count_o,count_x = 0,0
    for i in range(n):
        if board[i][n-1-i] == "o":
            count_o += 1
        else:
            if board[i][n-1-i] == "x":
                count_x += 1
    if count_o == n:
        return 0
    else:
        if count_x == n:
            return 1
    return -1


board = [["o", "o", "o"],
         ["x", "x", " "],
         [" ", "x", "x"]]

result = tic_tac_win(board)
print result

board[0][0] = "x"
result = tic_tac_win(board)
print result

board[1][1] = "o"
result = tic_tac_win(board)
print result


board = [["o", "o", "o", "x"],
             ["x", "x", "o", "o"],
             ["x", " ", "x", "x"],
             ["o", "x", "o", "x"]]
result = tic_tac_win(board)
print result

board[0][3] = "o"
result = tic_tac_win(board)
print result

board[0][0] = "x"
result = tic_tac_win(board)
print result

board[2][2] = "o"
result = tic_tac_win(board)
print result

