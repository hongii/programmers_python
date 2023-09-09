# 알고리즘 : bfs
# 문제 이해 못해서 시간 오래 걸림..&& visited 배열 처리 제대로 처리 못해서 테케2번 무한루프 돌아서 이동시키는 부분 다른사람 풀이 조금 참고함
# 첫번째 코드 -> correct, 2번째 코드 보다는 느린편
from collections import deque
def bfs(board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dq = deque()
    visited = [[0]*len(board[0]) for _ in range(len(board))]
    row, col = len(board), len(board[0])
    
    for i in range(len(board)):
        if "R" in board[i]:
            start_x = i
            start_y = board[i].index("R")
            dq.append((start_x, start_y))
            visited[start_x][start_y] = 1
            break
    
    while dq:
        x, y = dq.popleft()
        if board[x][y] == "G":
            return visited[x][y] - 1
        
        for i in range(4):
            nx, ny = x, y
            while True:
                x_ = dx[i] + nx
                y_ = dy[i] + ny
                if (0 <= x_ < row and 0 <= y_ < col and board[x_][y_] == "D") or ( x_ >= row or x_ < 0 or 0 > y_ or y_ >= col):
                    if not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        dq.append((nx, ny))
                    break
                else:
                    nx, ny = x_, y_
    return -1
    
    
def solution(board):
    board = [list(board[i]) for i in range(len(board))]
    return bfs(board)




# 두번째 코드 -> correct, 다른 사람들 풀이 조금씩 참고(visited 배열 대신 set 사용)
from collections import deque
def bfs(board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dq = deque()
    visited = set()
    row, col = len(board), len(board[0])
    
    for i in range(len(board)):
        if "R" in board[i]:
            start_x, start_y = i, board[i].index("R")
            dq.append((start_x, start_y, 0))
            break
    
    while dq:
        x, y, cnt = dq.popleft()

        if board[x][y] == "G":
            return cnt
        
        visited.add((x, y))
        for i in range(4):
            x_ = dx[i] + x
            y_ = dy[i] + y
            while 0 <= x_ < row and 0 <= y_ < col and board[x_][y_] != "D": # 벽이나 "D"를 만나기 전까지 슬라이딩
                x_ += dx[i]
                y_ += dy[i]
                
            if (x_-dx[i], y_-dy[i]) not in visited:
                dq.append((x_-dx[i], y_-dy[i],cnt+1))
                visited.add((x_-dx[i], y_-dy[i])) 
    return -1
    
    
def solution(board):
    board = [list(board[i]) for i in range(len(board))]
    return bfs(board)