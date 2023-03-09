def solution(d, budget):
    d.sort()
    total, cnt = 0, 0
    for i in range(len(d)):
        total += d[i]
        cnt += 1
        if total > budget:
            cnt -= 1
            total -= d[i]
            break
    return cnt