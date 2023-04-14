def isPrime(x):
    if x == 1:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    res = []
    convert = ""
    while n > 0:
        convert += str(n % k)
        n = n // k
    convert = convert[::-1]

    convert = convert.replace("0", ".")
    res = convert.split(".")
    cnt = 0
    for x in res:
        if x == "":
            continue
        if isPrime(int(x)):
            cnt += 1

    return cnt  