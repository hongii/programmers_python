# LV 2 문제의 멀리 뛰기 문제와 유사. 하지만 이 문제는 dp를 이용하여 '피보나치 수열'을 구현하지 않으면 시간초과남
# sol 1) 변수 2개만 사용하여 피보나치 수열 문제 풀기 -> 효율성 good
def solution(n):
    a, b = 1, 1
    for _ in range(2, n+1):
        a, b = b, (a+b) % 1000000007 # 값을 더할때마다 해당 값으로 나눠준 결과값을 b에 할당하면 효율성이 더 좋아진다.(해당 값으로 안나눠주면 효율성 테스트에서 시간이 더 걸림)

    return b % 1000000007


# sol 2) 리스트에 저장하면서 dp의 bottom-up방식으로 피보나치 수열 구현
def solution(n):
    dp_fibo = [0] * (n+2)
    dp_fibo[1], dp_fibo[2] = 1, 1
    for i in range(3, n+2):
        dp_fibo[i] = (dp_fibo[i-1] + dp_fibo[i-2]) % 1000000007

    return dp_fibo[n+1] % 1000000007


''' 첫번째 시도 -> 테케는 전부 통과했으나 효율성 테스트 전부 시간초과로 실패
def solution(n):
    facto = [1]*(n+1)
    for i in range(2, n+1):
        facto[i] = facto[i-1] * i 

    res = 0
    w = n//2 # 가로방향 타일 갯수
    for i in range(n//2, -1, -1):
        h = n - w*2 # 세로 방향 타일 갯수
        if h == 0 or w == 0:
            res += 1
        else:
            res += facto[h+w] // (facto[h]*facto[w])
        w -= 1
    return res % 1000000007

'''
