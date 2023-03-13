import itertools as it
def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
        
def solution(nums):
    res = []
    cnt = 0
    for x in it.combinations(nums, 3):
        if isPrime(sum(x)):
            cnt += 1
    return cnt