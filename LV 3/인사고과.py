# 두번째 풀이 -> 다른 사람 풀이 참고
def solution(scores):
    res = 0
    wanho = scores[0]
    scores.sort(key=lambda x:(-x[0], x[1])) # 근무태도는 내림차순, 동료 평가는 오름차순 정렬
    maxAttitude = 0 # scores배열에서 앞에 위치한 요소일수록 근무태도는 높은 점수이므로, 뒤에 위치한 요소일수록 근무태도 점수는 낮음이 보장된다. 따라서, 앞서 나온 요소들의 동료 평가 점수중 가장 큰 점수와 비교해서 해당 요소의 점수가 더 낮다면 인센티브 못받음  
    for score in scores:
        # 완호가 인센티브 못받는 경우 -> 어떤 사원의 두 점수보다 완호의 두 점수가 모두 낮은 경우
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        
        # 인센티브 못받는 사원은 걸러짐 -> 여태 앞에서 등장한 사원들의 동료평가 최대 점수(maxAttitude)보다 현재 사원의 동료 평가 점수가 더 낮은 점수인 경우는 아래 코드 수행안함
        if maxAttitude <= score[1]:
            # 완호의 등수 구하기
            if wanho[0]+wanho[1] < score[0]+score[1]:
                res += 1
            maxAttitude = score[1]
    return res+1


'''첫번째 풀이 -> 테케 21, 24, 25에서 시간초과...이중for문에서 100000^2 때문에 시간 초과 나는 듯
from collections import deque
def solution(scores):
    wanho = scores[0]
    filteredScores = []
    for i, a in enumerate(scores):
        for j, b in enumerate(scores):
            if i != j:
                if a[0] < b[0] and a[1] < b[1]:
                    break
        else:
            filteredScores.append(a)
                    
    if wanho not in filteredScores:
        return -1
    else:
        filteredScores.sort(key=lambda x:(x[0]+x[1]), reverse=True)
        filteredScores = deque(filteredScores)
        res = 0
        while filteredScores:
            now = filteredScores.popleft()
            res += 1
            if now == wanho:
                break
        return res

'''