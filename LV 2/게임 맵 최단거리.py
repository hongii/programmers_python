# 평소 풀던대로 idx = 게임맵 좌표 - 1 -----> (1, 1)에서 시작하는게 아니라 (0, 0)에서 시작 & 도착 좌표는 (row-1, col-1)
from collections import deque
def bfs(maps, row, col):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dq = deque()
    visited = [[False]*(col) for _ in range(row)]
    distance = [[10e5]*(col) for _ in range(row)]  
    
    dq.append([0, 0])
    visited[0][0] = True
    distance[0][0] = 1
    while dq:
        now = dq.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0 <= x < row and 0 <= y < col and not visited[x][y] and maps[x][y] == 1:
                distance[x][y] = distance[now[0]][now[1]] + 1
                visited[x][y] = True
                dq.append([x, y])
                if x == row-1 and y == col-1:
                    return distance[x][y]
    return distance[row-1][col-1] if distance[row-1][col-1] != 10e5 else -1
        
def solution(maps):   
    row, col = len(maps), len(maps[0])
    return bfs(maps, row, col)


'''첫번째 풀이 -> 게임맵의 idx와 좌표번호 일치시키기 위해 row와 col을 하나씩 추가시킴..(근데 굳이 왜 이렇게 했을까..?)
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
'''