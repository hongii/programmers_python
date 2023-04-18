# bfs 이용한 두번째 풀이 -> 통과
from collections import deque
def bfs(a, b, arr):
    global dis, check, isOK
    dq = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dis[a][b] = 0
    dq.append([a, b])

    while dq:
        now = dq.popleft()
        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]
            if 0 <= x < 5 and 0 <= y < 5 and check[x][y] == False:
                if arr[x][y] == "O":
                    dis[x][y] = dis[now[0]][now[1]] + 1
                    check[x][y] = True
                    # print(x, y,dis[x][y])
                    dq.append([x, y])
                
                elif arr[x][y] == "P":
                    dis[x][y] = min(dis[now[0]][now[1]] + 1, dis[x][y])
                    # print(x, y,dis[x][y])
                    if dis[x][y] <= 2:
                        isOK = 0
                        return isOK
    return isOK

def solution(places):
    global dis, check, isOK
    res = []
    size = len(places)
    for num in range(size):
        dis = [[11]*5 for _ in range(5)]
        check = [[False]*5 for _ in range(5)]
        arr = places[num]
        isOK = 1
        for i in range(5):
            for j in range(5):
                if arr[i][j] == "P" and check[i][j] == False:
                    check[i][j] = True
                    isOK = bfs(i, j, arr)
                    if isOK == 0:
                        break
            if isOK == 0:
                break
        res.append(isOK)
    return res

'''
# dfs 이용한 첫번째 풀이 -> 통과
import sys
sys.setrecursionlimit(10 ** 6)
def dfs(a, b, arr):
    global dis, check, isOK
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < 5 and 0 <= y < 5 and check[x][y] == False:
            if arr[x][y] == "O":
                dis[x][y] = dis[a][b] + 1
                check[x][y] = True
                # print(x, y,dis[x][y])
                isOK = dfs(x, y, arr)
                check[x][y] = False
            
            elif arr[x][y] == "P":
                dis[x][y] = min(dis[a][b] + 1, dis[x][y])
                # print(x, y,dis[x][y])
                if dis[x][y] <= 2:
                    isOK = 0
                    return isOK

    return isOK

def solution(places):
    global dis, check, isOK
    res = []
    size = len(places)
    for num in range(size):
        dis = [[11]*5 for _ in range(5)]
        check = [[False]*5 for _ in range(5)]
        arr = places[num]
        isOK = 1
        for i in range(5):
            for j in range(5):
                if arr[i][j] == "P" and check[i][j] == False:
                    dis[i][j] = 0
                    check[i][j] = True
                    isOK = dfs(i, j, arr)
                    if isOK == 0:
                        break
            if isOK == 0:
                break
        res.append(isOK)
    return res
'''
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])  )