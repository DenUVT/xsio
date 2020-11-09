from copy import deepcopy

board = [[None] * 3, [None] * 3, [None] * 3]


def generateNextMoves(board):
    xy_copy = []
    xy = []
    board_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] is None:
                board_copy = deepcopy(board)
                board_copy[i][j] = 'o'
                xy.append(i)
                xy.append(j)
                board_list.append(board_copy)
    xy_copy.append(xy)
    print(xy_copy)
    return board_list

def generateNextMovesXY(board):
    xy_copy = []
    xy = []

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] is None:
                xy.append(i)
                xy.append(j)
                xy_copy.append(deepcopy(xy))
                xy.clear()

    return xy_copy



def hfunction(board):
    score = 0
    res=[]
    # block
    for i in range(0, 3):

        score -= 10 if board[i][:].count('x') == 2 and board[i][:].count(None) == 1 else 0
       # for j in range (0,3):
        res.append([sub[i] for sub in board]) #column
    for i in range ( 0,3):
        score -= 10 if res[i].count('x') == 2 and res[i].count(None) == 1 else 0
        #res.clear()

    score -= 10 if board[1][1] is 'x' and board[2][2] is 'x' and board[0][0] is None or \
                   board[0][0] is 'x' and board[1][1] is 'x' and board[2][2] is None or \
                   board[2][2] is 'x' and board[0][0] is 'x' and board[1][1] is None \
        else 0

    score -= 10 if board[1][1] is 'x' and board[2][0] is 'x' and board[0][2] is None or \
                   board[0][2] is 'x' and board[1][1] is 'x' and board[2][0] is None or \
                   board[2][0] is 'x' and board[0][2] is 'x' and board[1][1] is None \
        else 0



    #  win
    for i in range(0, 3):
        score += 100 if board[i][:].count('o') == 3 else 0
       #for j in range (0,3):
        res.append([sub[i] for sub in board]) #column
    for i in range (0,3):

        score += 100 if res[i].count('o') == 3 else 0

    score += 100 if board[1][1] is 'o' and board[2][2] is 'o' and board[0][0] is 'o' else 0

    score += 100 if board[1][1] is 'o' and board[2][0] is 'o' and board[0][2] is 'o' else 0



    # #  not win
    for i in range(0, 3):
        score += 1 if board[i].count('o') == 1 and board[i].count(None) == 2 else 0
        #for j in range (0,3):
        res.append([sub[i] for sub in board])
    for i in range (0,3) :
        score += 1 if res[i].count('o') == 1 and res[i].count(None) == 2 else 0

    for i in range(0, 3):
        score += 2 if board[i][:].count('o') == 2 and board[i].count(None) == 1 else 0
        #for j in range (0,3):
        res.append([sub[i] for sub in board])
    for i in range  (0,3):
        score += 2 if res[i].count('o') == 2 and res[i].count(None) == 1 else 0

    score += 2 if board[1][1] is 'o' and board[2][2] is 'o' and board[0][0] is None or \
                  board[0][0] is 'o' and board[1][1] is 'o' and board[2][2] is None or \
                  board[2][2] is 'o' and board[0][0] is 'o' and board[1][1] is None \
        else 0

    score += 2 if board[1][1] is 'o' and board[2][0] is 'o' and board[0][2] is None or \
                  board[0][2] is 'o' and board[1][1] is 'o' and board[2][0] is None or \
                  board[2][0] is 'o' and board[0][2] is 'o' and board[1][1] is None \
        else 0

    score += 1 if board[1][1] is 'o' and board[2][2] is None and board[0][0] is None or \
                  board[0][0] is 'o' and board[1][1] is None and board[2][2] is None or \
                  board[2][2] is 'o' and board[0][0] is None and board[1][1] is None \
        else 0

    score += 1 if board[1][1] is 'o' and board[2][0] is None and board[0][2] is None or \
                  board[0][2] is 'o' and board[1][1] is None and board[2][0] is None or \
                  board[2][0] is 'o' and board[0][2] is None and board[1][1] is None \
        else 0

    return score

def test(board):
    for i in generateNextMoves(board):
        for j in i:
            print(j)
        print(hfunction(i))
