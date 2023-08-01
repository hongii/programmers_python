# 2회차 코드
def solution(number, k):
    s = []
    for i in range(len(number)):
        while s and k and number[i] > s[-1] :
            s.pop()
            k -= 1
        s.append(number[i])
        
    if k > 0:
        s = s[:-k]
    return "".join(s)



# 1회차 코드
# 그리디(탐욕법) -> stack이용 (다른사람 풀이 참고)
def solution(number, k):
    stack = []
    for n in number:
        # stack의 top에 위치한 값이 현재 숫자(n)보다 작은 경우, n보다 크거나 같은 수가 나올때까지 pop()수행
        while stack and stack[-1] < n and k > 0:
            k -= 1
            stack.pop()
        stack.append(n)

    # 아직 제거 해야할 횟수가 남은경우, 일의자리 숫자부터 제거
    if k > 0:
        while k > 0 :
            k -= 1
            stack.pop()

    return "".join(stack)


''' 시간 초과 발생 -> number의 자릿수가 100만 이므로 combinations() 사용 시 시간초과 발생
from itertools import combinations
def solution(number, k):
    size = len(number) - k
    cb = list(combinations(list(number), size))
    cb.sort(reverse=True)
    return "".join(cb[0])
'''