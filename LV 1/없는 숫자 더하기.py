def solution(numbers):
    res = 0
    check = [0] * 10
    for i in range(len(numbers)):
        check[numbers[i]] = 1
    for i in range(10):
        if check[i] == 0:
            res += i
            
    return res

''' 최적의 코드
def solution(numbers):
    return sum(range(10)) - sum(numbers)
'''