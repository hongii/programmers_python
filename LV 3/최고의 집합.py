def solution(n, s):
    res = []
    if s//n == 0:
        return [-1]
    
    while s:
        res.append(s//n)
        s = s - s//n
        n -= 1
    return res
'''
# 두번째로 구현한 코드 풀이(참고한 풀이x)
합이 s가 되는 숫자 조합들 중에 제곱수의 값이 가장 곱이 큰 수가 된다.
ex1) s = 25, n = 2 -> 5*5 = 25 > 4*6 = 24
ex2) s = 18, n = 4 -> 4*4*5*5 = 400 > 4*4*4*6 = 384     --------> 5+5 = 10, 4+6 = 10 이라서 두 수의 합은 동일하지만 5의 제곱값이 4*6의 값보다 크다.
    즉, s를 n으로 나눈 몫을 구하고, s에서 그 몫을 뺸 나머지 값에서 다시 n으로 나눈 몫을 구하고...를 반복하면 
    합이 s가 되는 n개의 숫자 조합 중 곱이 가장 큰 숫자 조합을 구할 수 있다.
'''


''' 첫번째 코드 -> 시간초과
from itertools import combinations_with_replacement
def solution(n, s):
    res = [-1]
    nums = list(range(1, s+1))
    cb = list(combinations_with_replacement(range(1, s+1), n))
    maxRes = 0
    for c in cb:
        if sum(c) == s:
            mul = 1
            for num in c:
                mul *= num
            if maxRes < mul:
                maxRes = mul
                res = list(c)
    return res
'''