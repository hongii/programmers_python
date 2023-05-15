# 효율성 테스트 전부 시간초과.... -> 미해결
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def divisor(x):
    div = []
    MAX = 1e7
    for i in range(1, x//2 + 1):
        if i >= MAX:
            break
        if x % i == 0:
            div.append(i)
    return div

def solution(begin, end):
    res = []
    for i in range(begin, end+1):
        if i == 1:
            res.append(0)
        elif isPrime(i):
            res.append(1)
        else:
            div = divisor(i)
            res.append(div[-1])
    return res