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