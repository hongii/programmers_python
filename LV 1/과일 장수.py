def solution(k, m, score):
    score.sort(reverse=True)
    maxProfit = 0
    for i in range(0, len(score), m):
        if len(score[i:i+m]) != m:
            break
        maxProfit += min(score[i:i+m]) * m
    return maxProfit