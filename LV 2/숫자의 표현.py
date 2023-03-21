# 수학적 사고 필요
# => '주어진 자연수를 연속되는 자연수들의 합으로 표현할 수 있는 방법의 수는 주어진 자연수의 약수 중에서 홀수인 수의 개수와 같다.'를 이용
# => 즉,  주어진 수 n까지 for 반복문을 돌면서, i가 n의 약수 이면서 홀수인 경우일 때의 그 횟수를 증가시키는 방법
# ex) 15의 약수 -> 1, 3, 5, 15 중에서 홀수인 약수의 갯수 : 4 ---> 따라서, n이 15인 경우, 연속되는 자연수들의 합으로 n을 표현할 수 있는 방법의 수는 4이다.

def solution(n):
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0 and i%2 == 1:
            cnt += 1
    return cnt