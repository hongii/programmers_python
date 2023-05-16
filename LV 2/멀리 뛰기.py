''' 내가 짠 코드의 풀이조건 -> 같은것이 있는 순열 구하는 공식 이용
# 같은 것이 있는 순열 구하는 공식
순열이 같은 것이 포함된 원소들을 나열하는 경우의 수는 나열하는 원소의 팩토리얼에 중복된 원소들의 팩토리얼을 나누어주면 된다.
예를 들어 aaabb와 같은 경우 a가 3개이고 b가 2개이므로 5!을 3!와 2!로 나누어주면 된다.
ex) [a, a, a, b, b] -> 5! / 3!2! = 10
'''

def solution(n):
    res = 0
    dp_facto = [1]*(n+1)
    for i in range(2, n+1):
        dp_facto[i] = dp_facto[i-1]*i
        
    for i in range(n//2 + 1):
        cntOne = n - i*2
        arr = [1]*cntOne + [2]*i
        if all(x == 1 for x in arr) or all(x == 2 for x in arr):
            res += 1
        else:
            res += dp_facto[len(arr)] // (dp_facto[cntOne] * dp_facto[i])
    return res % 1234567

####################################################################################################

''' 다른 사람의 풀이 -> 피보나치 수열 이용
이 문제의 테스트 케이스의 일부를 아래의 예시로 확인하면,
n = 1, result = 1
n = 2, result = 2
n = 3, result = 3
n = 4, result = 5
n = 5, result = 8
n = 6, result = 13
n = 7, result = 21
n = 8, result = 34
n이 1부터 8번 까지의 테스트케이스 결과값은 위와 같다.

1, 2, 3, 5, 8, 13, 21, 34 ... -> 이는 피보나치 수열과 유사하다.
이 수열의 맨 앞에 1만 하나 더 붙이면 피보나치 수열 그 자체가 되는 것이다.
1, 1, 2, 3, 5, 8, 13, 21, 34 ...
=> 1, 1, (1+1), (1+2), (2+3), (3+5), (5+8), (8+13), (13+21)
dp를 이용하여 피보나치 수열을 구현하면 된다.

# 위의 해설을 이용한 두번째 코드
def solution(n):
    dp_fibo = [0] * (n+2)
    dp_fibo[1], dp_fibo[2] = 1, 1
    for i in range(3, n+2):
        dp_fibo[i] = dp_fibo[i-1] + dp_fibo[i-2]
    
    return dp_fibo[n+1] % 1234567
'''