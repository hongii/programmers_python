def solution(number, limit, power):
    total = 0
    for i in range(1, number+1):
        divisorCnt = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                divisorCnt += 1
                if j != i//j:
                    divisorCnt += 1
        if divisorCnt <= limit:
            total += divisorCnt
        else:
            total += power
    return total