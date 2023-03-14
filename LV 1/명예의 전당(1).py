def solution(k, score):
    hof = []
    minScore = []
    for i in range(len(score)):
        if len(hof) < k:
            hof.append(score[i])
            minScore.append(min(hof))
        else:
            if min(hof) < score[i]:
                hof.remove(min(hof))
                hof.append(score[i])
                
            minScore.append(min(hof)) 
    return minScore