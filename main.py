board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# function to print broad
def Print_board(board):
    print('\n')
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")  # no "\n"
            
            if(j == len(board[0]) - 1):
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")

# find the empty cell on the board
def Find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # (row, col)
    return None

# check at the given position (pos), whether the grid is valid with
# it's value (num). 
def Valid(board, num, pos):
    # check row
    for j in range(len(board[0])):
        if board[pos[0]][j] == num and j != pos[1]:
            return False
        
    # check col
    for i in range(len(board)):
        if board[i][pos[1]] == num and i != pos[0]:
            return False
    
    # check block
    rank = pos[0] // 3
    stack = pos[1] // 3
    block_rows = range(rank * 3, rank * 3 + 3)
    block_cols = range(stack * 3, stack * 3 + 3)
    for i in block_rows:
        for j in block_cols:
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

# solve the problem using backtracking
def Solve(board):
    find = Find_empty(board)
    if not find:
        return True # we found the solution
    else:
        row, col = find

    for i in range(1, 10):
        if Valid(board, i, (row, col)):
            board[row][col] = i

            if Solve(board):
                return True
            
            board[row][col] = 0

    return False
        


Print_board(board)
Solve(board)
Print_board(board)