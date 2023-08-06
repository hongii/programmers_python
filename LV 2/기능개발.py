# 2회차 코드_1 => stack을 사용한 풀이
import math
def solution(progresses, speeds):
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    s, res = [], []
    i = 0
    cnt = 0
    while i < len(days):
        if s and s[0] < days[i]: 
            res.append(cnt)
            s = [days[i]]
            cnt = 1
            i += 1
        else:
            s.append(days[i])
            cnt += 1
            i += 1
        
    if s:
        res.append(len(s))
        
    return res


# 2회차 코드_2 => stack없이 변수만 사용, 앞쪽 기능의 기능완료일(comp)과 다음 기능의 작업일 수(days[i])를 비교 
import math
def solution(progresses, speeds):
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    res = []
    comp = days[0]
    i, cnt = 1, 1
    while i < len(days):
        if comp < days[i]: 
            res.append(cnt)
            comp = days[i]
            cnt = 1
            i += 1
        else:
            cnt += 1
            i += 1
        
    if cnt > 0:
        res.append(cnt)
        
    return res


# 1회차 코드
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