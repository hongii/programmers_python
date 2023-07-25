# 두번째 풀이 -> 2회차
from itertools import combinations
from collections import Counter
def solution(orders, course):
    res = []
    for x in course:
        counter = Counter()
        for order in orders:
            cb = Counter(combinations(sorted(order), x))
            counter += cb
        if not counter: continue
            
        sortedCounter = counter.most_common()
        maxCnt = sortedCounter[0][1]
        for tup, cnt in sortedCounter:
            if cnt == maxCnt and maxCnt > 1:
                res.append("".join(list(tup)))
            else: 
                break
    return sorted(res)

''' 첫번째 코드
from itertools import combinations
def solution(orders, course):
    res = []
    for menuCnt in course:
        total = {}
        for order in orders:
            if len(order) >= menuCnt:
                cb = list(combinations(sorted(list(order)), menuCnt))
                for x in cb:
                    if x not in total.keys():
                        total[x] = 1
                    elif x in total.keys():
                        total[x] += 1

        if len(total) > 0:
            sortedTotal = sorted(total.items(), key=lambda x:x[1], reverse=True)
            maxCnt = sortedTotal[0][1]
            if maxCnt > 1:
                res.append("".join(list(sortedTotal[0][0])))
                for i in range(1, len(sortedTotal)):
                    k, v = sortedTotal[i][0], sortedTotal[i][1]
                    if v >= maxCnt:
                        res.append("".join(list(k)))
                    else:
                        break

    res.sort()
    return res
'''