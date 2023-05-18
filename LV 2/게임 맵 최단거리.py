from collections import deque
def bfs(maps, row, col):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dq = deque()
    visited = [[False]*(col+1) for _ in range(row+1)]
    distance = [[10e5]*(col+1) for _ in range(row+1)]  

    dq.append([1, 1])
    visited[1][1] = True
    distance[1][1] = 1
    while dq:
        now = dq.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0 < x <= row and 0 < y <= col and not visited[x][y] and maps[x][y] == 1:
                distance[x][y] = distance[now[0]][now[1]] + 1
                visited[x][y] = True
                dq.append([x, y])
                if x == row and y == col:
                    return distance[x][y]
    return distance[row][col] if distance[row][col] != 10e5 else -1

def solution(maps):   
    row, col = len(maps), len(maps[0])
    maps.insert(0,[0]*(col+1))
    for i in range(1, row+1):
        maps[i].insert(0, 0)

    return bfs(maps, row, col)