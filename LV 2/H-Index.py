def solution(citations):
    HIndex = 0
    for i in range(len(citations)+1):
        cnt = 0
        for n in citations:
            if i <= n:
                cnt += 1 
        if i <= cnt:
            if HIndex < i:
                HIndex = i

    return HIndex
