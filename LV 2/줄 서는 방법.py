# factorial과 순열을 이용한 규칙 -> factorial은 dp로 저장해두고 k를 이용하여 자릿수 뽑아내기..(다른 사람 풀이 참고)
def solution(n, k):
    dp_facto = [1]*(n+1)
    for i in range(2, n+1):
        dp_facto[i] = dp_facto[i-1]*i

    res = []
    nums = list(range(1, n+1))
    while n:
        res.append(nums[(k-1)//dp_facto[n-1]])
        nums.pop((k-1)//dp_facto[n-1])
        k = (k-1) % dp_facto[n-1] + 1
        n -= 1
    return res
# 해설 참고한 사이트 링크 : https://sjy4388.tistory.com/63 , https://velog.io/@longroadhome/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.3-%EC%A4%84-%EC%84%9C%EB%8A%94-%EB%B0%A9%EB%B2%95-JS



'''첫번째 시도: 순열 라이브러리 사용-> 테케 2개 시간초과, 효율성 테스트 시간초과로 불통과
from itertools import permutations
def solution(n, k):
    pm = list(permutations(range(1, n+1), n))
    pm.sort()
    return list(pm[k-1])
'''

'''두번째 시도: 완전탐색(dfs) -> 첫번째 시도보다 더 시간 오래 걸림, 효율성 테스트 시간초과로 불통과
import copy
def dfs(x, n):
    global nums, check, res, tmp
    if x == n+1:
        res.append(copy.deepcopy(tmp))
    else:
        for i in range(1, n+1):
            if check[i] == False:
                check[i] = True
                tmp.append(i)
                dfs(x+1, n)
                check[i] = False
                tmp.pop()
                
def solution(n, k):
    global nums, check, res, tmp
    check = [False]*(n+1)
    tmp, res = [], []
    nums = list(range(1, n+1))
    dfs(1, n)
    return sorted(res)[k-1]
'''