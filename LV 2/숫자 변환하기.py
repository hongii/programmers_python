# dp 사용하는 아이디어 -> 다른사람 풀이 참고함
def solution(x, y, n):
    inf = float('inf')
    dp = [inf] * (y+1)
    dp[x] = 0
    for i in range(x, y+1):
        if i+n <= y:
            dp[i+n] = min(dp[i]+1, dp[i+n])
        if i*2 <= y:
            dp[i*2] = min(dp[i]+1, dp[i*2])
        if i*3 <= y:
            dp[i*3] = min(dp[i]+1, dp[i*3])

    return dp[y] if dp[y] != inf else -1