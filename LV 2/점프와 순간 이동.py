def solution(n):
    jump = 0
    while n > 0:
        if n % 2 == 1: # n값이 홀수인 경우 -> 점프하기(-1 해줘서 짝수만들기)
            n -= 1
            jump += 1
        n //= 2
    return jump