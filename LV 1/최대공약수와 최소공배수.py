import math
def solution(n, m):    
    gcd = math.gcd(n,m)
    return [gcd, (n*m)//gcd]

'''
유클리드 호제법을 이용한 최대공약수 구현 코드 참고
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
'''