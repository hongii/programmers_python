# 두번째 코드 -> dp이용
def solution(land):
    n = len(land)
    dp = [[0]*4 for _ in range(n)]
    for j in range(4): # dp 초기화
        dp[0][j] = land[0][j]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + land[i][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + land[i][2]
        dp[i][3] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + land[i][3]
    return max(dp[n-1])


''' 첫번째 코드 -> dfs 이용: 문제 예제는 통과하지만 코드 제출시 모든 테케와 효율성 테스트에서 런타임에러 및 시간초과로 실패함
def dfs(x, y, land):
    global n, score, MAX
    if x == n-1:
        if score > MAX:
            MAX = score
    else:
        for j in range(4):
            if y == j:
                continue
            else:
                score += land[x+1][j]
                dfs(x+1,j,land)
                score -= land[x+1][j]
    
def solution(land):
    global n, score, MAX
    MAX = 0
    n = len(land)
    for y in range(4):
        score = land[0][y]
        dfs(0, y, land)
    return MAX
'''