# 2회차 풀이 -> 분할 정복
def divideConquer(x, y, size, arr):
    global zeroCnt, oneCnt 
    if size > 1 and all(arr[i][j] == 1 for i in range(x, x+size) for j in range(y, y+size)):
        oneCnt += 1
        return
    if size > 1 and all(arr[i][j] == 0 for i in range(x, x+size) for j in range(y, y+size)):
        zeroCnt += 1
        return
    
    if size == 1:
        if arr[x][y] == 1:
            oneCnt += 1
        else:
            zeroCnt += 1
    
    else:
        size //= 2
        divideConquer(x, y, size, arr)
        divideConquer(x+size, y, size, arr)
        divideConquer(x, y+size, size, arr)
        divideConquer(x+size, y+size, size, arr)
            
    
def solution(arr):
    global zeroCnt, oneCnt 
    zeroCnt, oneCnt = 0, 0
    divideConquer(0, 0, len(arr), arr)
    return [zeroCnt, oneCnt]


# 1회차 풀이
import sys
sys.setrecursionlimit(10**6)
def compression(x1, x2, y1, y2, arr):
    global cntZero, cntOne
    mx, my = (x1+x2) // 2, (y1+y2) // 2
    # print(x1,mx, x2, y1, my,y2)
    if x1 >= x2 or y1 >= y2:
        if arr[x1][y1] == 1:
            cntOne += 1
        elif arr[x1][y1] == 0:
            cntZero += 1
        print(cntZero,cntOne)
            
    else:
        if all(arr[i][j] == 0 for i in range(x1, x2+1) for j in range(y1, y2+1)):
            cntZero +=1
        elif all(arr[i][j] == 1 for i in range(x1, x2+1) for j in range(y1, y2+1)):
            cntOne +=1
        else:
            compression(x1, mx, y1, my, arr)
            compression(mx+1, x2, y1, my, arr)
            compression(x1, mx, my+1, y2, arr)
            compression(mx+1, x2, my+1, y2, arr)
    return

def solution(arr):
    global cntZero, cntOne
    cntZero, cntOne = 0, 0
    compression(0, len(arr)-1, 0, len(arr)-1, arr)
    
    return [cntZero, cntOne]

# solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])