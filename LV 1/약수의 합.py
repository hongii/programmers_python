def solution(n):
    answer = 0
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    answer = sum(divisor)
    
    return answer