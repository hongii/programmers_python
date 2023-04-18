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
# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])  )