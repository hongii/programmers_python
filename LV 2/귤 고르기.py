from collections import Counter
def solution(k, tangerine):
    dic = Counter(tangerine)
    cnt, res = 0, 0
    for t in dic.most_common():
        if cnt < k:
            cnt += t[1]
            res += 1
        else:
            break

    return res

'''
Counter의 사용법 추가
1. most_common(n)함수는 입력된 값의 요소들 중 빈도수(최빈값)을 n개 반환한다. 최빈값을 반환하므로 빈도수가 높은 순으로 상위 n개를 반환하며, 결과값은 Tuple자료형이다.
=> most_common() 빈 값이면 요소 전체를 반환한다.   
=> most_common(2) 최빈값 상위 2개를 반환한다.
=> most_common(1) 최빈값 상위 1개를 반환한다.
'''