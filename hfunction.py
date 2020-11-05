from copy import deepcopy

board = [[None]*3, [None]*3, [None]*3]

def generateNextMoves(board):
    board_list = []
    for i in range (0,3):
        for j in range (0,3):
            if board[i][j] is None:
                board_copy = deepcopy(board)
                board_copy[i][j]='o'
                board_list.append(board_copy)

    return board_list


print(generateNextMoves(board))




def hfunction(board):
    score=0
    #win
    for i in range(0,3):
        if board[i].count('x') == 3:
            score += 10
        if board[:][i].count('x') == 3:
            score +=10
    if board[1][1] is 'x':
        if board[2][2] is 'x':
            if board[0][0] is 'x':
               score += 10
    if board[1][1] is 'x':
        if board[2][0] is 'x':
            if board[0][2] is 'x':
                score += 10
