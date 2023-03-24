def isPossible(Xbingo, Obingo, cntX, cntO):
    # O가 이긴 경우, O의 갯수가 X의 갯수와 같으면 불가능 조건
    if Obingo > Xbingo and cntO == cntX:
        return 0
    
    # X가 이긴 경우, O의 갯수가 X의 갯수보다 많으면 불가능 조건
    elif Obingo < Xbingo and cntO > cntX:
        return 0
    
    # 동점인 경우,
    elif Obingo == Xbingo:
        # O와 X의 빙고갯수가 1개 이상으로 서로 같으나, O의 갯수가 X의 갯수보다 같거나 많으면 불가능 조건
        # ex) ["XXX", "XOO", "OOO"] -> X와 O모두 1빙고지만 O의 갯수가 X보다 많으므로 불가능 
        if Obingo != 0 and Xbingo != 0 and cntO >= cntX:
            return 0
        else:
            return 1
    else:
        return 1

def solution(board):
    if all(board[i] == "..." for i in range(3)):
        return 1
    
    cntX, cntO = 0, 0
    for x in board:
        cntX += x.count("X")
        cntO += x.count("O")
    if cntX > cntO or cntO > cntX + 1:
        return 0
    
    # 행 확인
    Xbingo, Obingo = 0, 0
    for x in board:
        if x == 'OOO':
            Obingo += 1
        if x == 'XXX':
            Xbingo += 1

    # 열 확인
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            Xbingo += 1
        if board[0][i] == board[1][i] == board[2][i] == "O":
            Obingo += 1
    
    # 대각선 확인
    if board[0][0] == board[1][1] == board[2][2] == "X":
        Xbingo += 1
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        Obingo += 1
    if board[0][2] == board[1][1] == board[2][0] == "X":
        Xbingo += 1
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        Obingo += 1
    print(Xbingo, Obingo, cntX, cntO)
    return isPossible(Xbingo, Obingo, cntX, cntO)