# 브루트포스 - 노가다..
from collections import deque
def solution(rows, columns, queries):
    board = [[] for _ in range(rows)]
    res = []
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            board[i-1].append((i-1)*columns + j)

    for site in queries:
        x1, y1, x2, y2 = site[0], site[1], site[2], site[3]

        # 행렬 테두리 값을 담는 리스트 만들기      
        tmp = deque()
        tmp.extend(board[x1-1][y1-1:y2])
        for i in range(x1, x2-1):
            tmp.append(board[i][y2-1])
        tmp.extend(board[x2-1][y1-1:y2][::-1])
        for i in range(x2-2, x1-1, -1):
            tmp.append(board[i][y1-1])

        tmp.appendleft(tmp.pop()) # 행렬 테두리 값을 시계방향으로 회전
        res.append(min(tmp))

        # 행렬 테두리 값 변경하기
        idx = 0
        for i in range(y1-1,y2):
            board[x1-1][i] = tmp[idx]
            idx += 1
        for i in range(x1, x2-1):
            board[i][y2-1] = tmp[idx]
            idx += 1
        for i in range(y2-1, y1-2, -1): 
            board[x2-1][i] = tmp[idx]
            idx += 1
        for i in range(x2-2, x1-1, -1):
            board[i][y1-1] = tmp[idx]
            idx += 1
    return res