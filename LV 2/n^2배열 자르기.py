def solution(n, left, right):
    res = []
    for i in range(left, right+1):
        x, y = i//n, i%n # 2차원 배열의 x좌표, y좌표
        res.append(max(x, y)+1) # 2차원 배열의 각 요소값은 max(x, y)에 1 더한 값

    return res

'''
예상했지만..당연히 시간초과..(입력값 n의 범위가 최대 10^7이므로 이중반복문 안돼!)
def solution(n, left, right):
    arr = [[0]*n for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(i):
            arr[i][j] = i+1
        for k in range(i, n):
            arr[i][k] = k+1
    
    for i in range(len(arr)):
        res.extend(arr[i])
    
    return res[left:right+1]
'''