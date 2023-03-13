def solution(N, stages):
    stages.sort()
    notClear = [0]
    res = []
    for i in range(1, N+1):
        if stages.count(i) == 0:
            notClear.append(0)
        else:
            notClear.append(stages.count(i))
            
    for i in range(1, len(notClear)):
        if notClear[i] == 0:
            res.append([0, i])
        else:
            stageTotalPlayer = len(stages) - sum(notClear[0:i])
            res.append([notClear[i]/stageTotalPlayer, i])
    
    res.sort(key = lambda x: (-x[0], x[1]))
    return list(x[1] for x in res)