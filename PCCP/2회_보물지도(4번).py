# bfs, 3차원 배열
from collections import deque
def solution(n, m, hole):
    global time, board
    time = [[[float('inf')] * 2 for j in range(n)] for i in range(m)] # time[i][j][0] -> (i, j)좌표로 이동할 때 신발 사용하지 않고 걸린시간, time[i][j][1] -> 신발 사용하고 걸린시간
    board = [[1]*n for _ in range(m)]
    for x, y in hole:
        board[y-1][x-1] = 0
        
    def bfs(n, m):
        global time, board
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        dq = deque()
        time[0][0][0] = 0 # (0,0)시작점에서의 시간은 0으로 초기화
        dq.append((0, 0, 0))
        
        while dq:
            x, y, jump = dq.popleft()
            for i in range(4):
                x_ = x + dx[i]
                y_ = y + dy[i]
                # 한칸 이동 => 신발사용 여부와 상관없이 전부 이동 가능(jump == 0 or jump == 1)
                if 0 <= x_ < m and 0 <= y_ < n and time[x_][y_][jump] > time[x][y][jump] + 1 and board[x_][y_]:
                    time[x_][y_][jump] = time[x][y][jump] + 1
                    dq.append((x_,y_,jump))
                
                # 신발 사용하는 경우 => 아직 신발을 사용하지 않은 경우에만 가능(jump == 0)
                xx_ = x_ + dx[i]
                yy_ = y_ + dy[i]
                if jump == 0 and 0 <= xx_ < m and 0 <= yy_ < n and time[xx_][yy_][1] > time[x][y][jump] + 1 and board[xx_][yy_]:
                    time[xx_][yy_][1] = time[x][y][jump] + 1
                    dq.append((xx_,yy_,1))

        return min(time[m-1][n-1][0], time[m-1][n-1][1])
    
    res = bfs(n, m)
    return res if res != float('inf') else -1