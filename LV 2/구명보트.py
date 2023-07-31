# 2회차 코드
def solution(people, limit):
    people.sort(reverse=True)
    l, r = 0, len(people)-1
    cnt = 0
    while l <= r:
        if people[l]+people[r] > limit:
            l += 1
        else:
            l += 1
            r -= 1
        cnt += 1
    return cnt



# 1회차 코드
# python_algorithm : [그리디 알고리즘] 침몰하는 타이타닉 문제와 유사 -> 다시 풀기
from collections import deque
def solution(people, limit):
    people.sort()
    weight = deque(people)
    cnt = 0
    while weight:
        if len(weight) == 1:
            cnt += 1
            break

        if weight[0] + weight[-1] > limit:
            weight.pop()
        else:
            weight.pop()
            weight.popleft()
        cnt += 1   

    return cnt 