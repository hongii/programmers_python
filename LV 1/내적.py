def solution(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])

''' zip()함수를 이용한 풀이
return sum([x*y for x, y in zip(a,b)])
'''