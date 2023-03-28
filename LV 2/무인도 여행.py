# 코딩 테스트에서 재귀를 사용할때는 아래의 코드는 선택이 아닌 필수이다.
# 파이썬의 재귀 최대 깊이의 기본 설정이 1,000회이므로, 이를 늘려주는 작업이 필요하다.
# 아래의 코드는 재귀 메모리 제한을 늘려주는 것이다. -> 재귀의 최대 깊이 설정값을 늘려주는 것
import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    global mapList
    global maxDays
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    row, col = len(mapList), len(mapList[0])

    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if 0 <= x_ < row and 0 <= y_ < col and mapList[x_][y_] != "X":
            maxDays += int(mapList[x_][y_])
            mapList[x_][y_] = "X"
            dfs(x_, y_)

def solution(maps):
    res = []
    global maxDays
    global mapList
    mapList = [list(x) for x in maps]

    for i in range(len(mapList)):
        for j in range(len(mapList[i])):
            maxDays = 0
            if mapList[i][j] != "X":
                maxDays = int(mapList[i][j])
                mapList[i][j] = "X"
                dfs(i, j)
                res.append(maxDays)
    return sorted(res) if len(res) != 0 else [-1]