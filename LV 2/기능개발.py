from collections import deque
import math
def solution(progresses, speeds):
    days = deque()
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))

    res = []
    while len(days) > 1:
        cnt = 1
        if days[0] < days[1]:
            days.popleft()
            res.append(cnt)
        else:            
            tmp = days.popleft()
            while days and tmp >= days[0]:
                days.popleft()
                cnt += 1
            res.append(cnt)

    if days: # days에 요소가 남아있다면, 추가로 마지막에 배포됨
        res.append(1)

    return res