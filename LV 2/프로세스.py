# 1회차 코드
from collections import deque
def solution(priorities, location):
    priorities = deque([[x, i] for i, x in enumerate(priorities)])
    cnt = 0
    [maxNum, maxIdx] = max(priorities)
    num, i = priorities[0][0], priorities[0][1]
    while priorities:
        # print(priorities)
        if maxNum == num:
            cnt += 1
            if i == location:
                break
            priorities.popleft()
            [maxNum, maxIdx] = max(priorities)
        else:
            priorities.append(priorities.popleft())
        num, i = priorities[0][0], priorities[0][1]

    return cnt


# 2회차 코드_2 -> 리스트 원소와 zip메서드 사용하여 우선순위 max 값 구하기
from collections import deque
def solution(priorities, location):
    dq = deque([[x, i] for i, x in enumerate(priorities)])
    print(list(zip(*dq))[0])
    maxPriority = max(list(zip(*dq))[0])
    cnt = 1
    print(maxPriority)
    while dq:
        p, i = dq.popleft()
        print(p, i, cnt, maxPriority)
        if p == maxPriority and i == location:
            return cnt
        if dq and p == maxPriority:
            print(dq)
            maxPriority = max(list(zip(*dq))[0])
            cnt += 1
        else:
            dq.append([p, i])
solution([1, 1, 1, 2], 2)      


# 2회차 코드_1 -> tuple 사용, dq에 튜플원소 한개 남은 경우엔 max메서드를 사용할 수 없으므로 조건 추가시킴
from collections import deque
def solution(priorities, location):
    dq = deque([(x, i) for i, x in enumerate(priorities)])
    maxPriority = max(*dq)[0]
    cnt = 1
    while dq:
        p, i = dq.popleft()
        if p == maxPriority and i == location:
            return cnt
        if dq and p == maxPriority:
            if len(dq) > 1: maxPriority = max(*dq)[0]
            else: maxPriority = dq[0][0]
            cnt += 1
        else:
            dq.append((p, i))
