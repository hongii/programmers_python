# 블록의 위치를 아래로 내리는 부분에서 막혀서 다른 사람 풀이 참고하여 다시 품
# 타겟 블록이 2*2 블록으로 고정되어 있으므로 BFS/DFS는 굳이 사용할 필요가 없다.
def solution(m, n, board):
    dx = [0, 1, 1] # x축 좌표: 우, 대각선아래, 아래
    dy = [1, 1, 0] # y축 좌표: 우, 대각선아래, 아래
    board = [list(board[i]) for i in range(m)]
    res = 0
    while True:
        blocks = set() # 2*2 블록이 겹치는 경우, 동일한 좌표가 중복으로 들어가지 않도록 set이용

        # board내에서 2*2 블록이 만들어지는 좌표를 set에 넣기
        for i in range(m-1):
            for j in range(n-1):
                b = board[i][j]
                if b == "":
                    continue
                elif board[i+dx[0]][j+dy[0]] == b and board[i+dx[1]][j+dy[1]] == b and board[i+dx[2]][j+dy[2]] == b:
                    blocks.add((i, j))
                    blocks.add((i+dx[0],j+dy[0]))
                    blocks.add((i+dx[1],j+dy[1]))
                    blocks.add((i+dx[2],j+dy[2]))

        # 타겟 블록의 갯수 == 집합에 존재하는 좌표의 갯수
        if len(blocks) > 0:
            res += len(blocks)
            for i, j in blocks:
                board[i][j] = ""
        else: # 더이상 제거할 블록이 없는 경우 -> 게임 종료
            break

        # board에서 제거된 블록이 있는 경우, 블록의 위치를 위에서 아래로 내려서 빈공간을 채움
        while True:
            flag = False
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] != ""  and board[i+1][j] == "":
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        flag = True
            if not flag:
                break
    # print(res)
    return res

# solution(6, 6, 	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])