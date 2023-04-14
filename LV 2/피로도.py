from itertools import permutations
def solution(k, dungeons):
    size = len(dungeons)
    pIdx = list(permutations(range(size), size)) # index 순열 
    maxCnt = 0
    for x in pIdx:
        cnt, cmp = 0, k
        for i in range(len(x)):
            np, cp = dungeons[x[i]][0], dungeons[x[i]][1]
            if cmp < np:
                break
            else:
                cmp -= cp
                cnt += 1
                
        if cnt > maxCnt:
            maxCnt = cnt
    
    return maxCnt
        