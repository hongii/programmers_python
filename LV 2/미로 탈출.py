from collections import deque
def bfs(start, end, maps):
    dq = deque()
    row, col = len(maps), len(maps[0])
    check = [[0]*col for _ in range(row)]
    distance = [[0]*col for _ in range(row)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(len(maps)): # 시작위치 좌표 찾고 dq에 넣기
        j = maps[i].find(start)
        if j != -1:
            dq.append((i, j))
            check[i][j] = 1
            break

    dis = 0
    while dq:
        now = dq.popleft()
        if maps[now[0]][now[1]] == end:
            dis = distance[now[0]][now[1]]
            break
        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]
            if 0 <= x < row and 0 <= y < col and check[x][y] == 0 and maps[x][y] != "X":
                dq.append((x, y))
                check[x][y] = 1
                distance[x][y] = distance[now[0]][now[1]] + 1
    return dis

def solution(maps):
    # 출발지점 ~ 레버까지
    StoL = bfs("S", "L", maps)

    # 레버 ~ 도착지점 
    LtoE = 0
    if StoL != 0:
        LtoE = bfs("L", "E", maps)
    return StoL+LtoE if StoL != 0 and LtoE != 0 else -1