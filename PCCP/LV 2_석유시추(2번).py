from collections import deque 
def solution(land):
    row, col = len(land), len(land[0])
    visited = [[False] * col for _ in range(row)] 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    result = [0]* col

    def bfs(x, y):
        visited[x][y] = True
        dq = deque()
        dq.append((x, y))
        oil_y_set = set()
        oil_y_set.add(y)
        mass_sum = 1
        
        while dq:
            x, y = dq.popleft()
            
            for i in range(4):
                x_ = x + dx[i]
                y_ = y + dy[i]
                if 0<= x_ < row and 0 <= y_ < col and land[x_][y_] == 1 and not visited[x_][y_] : 
                    visited[x_][y_] = True
                    dq.append((x_, y_))
                    oil_y_set.add(y_)
                    mass_sum += 1
        
        for i in oil_y_set:
            result[i] += mass_sum
        
    
    for i in range(row):
        for j in range(col):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)

    return  max(result)
