import itertools as it
def solution(number):
    cb = list(it.combinations(number,3))
    cnt = 0
    for a, b, c in cb:
        if (a + b + c) == 0:
            cnt += 1
    return cnt

'''최적의 풀이 -> combinations(number,3)의 경우, iterable한 객체를 반환하므로 굳이 list로 만들지 않아도 된다.
def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt
'''