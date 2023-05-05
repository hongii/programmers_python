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