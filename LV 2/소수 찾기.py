from itertools import permutations
def isPrime(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    cnt = 0
    cb = []
    for i in range(1, len(numbers)+1):
        tmp = list(permutations(numbers, i))
        cb.extend([int("".join(list(c))) for c in tmp])

    for c in set(cb):
        check = isPrime(c)
        if check:
            cnt += 1
    return cnt