import math
def arrayGCD(arr):
    gcd_ = 0
    for i in range(len(arr)):
        gcd_ = math.gcd(gcd_, arr[i])
    return gcd_

def solution(arrayA, arrayB):
    gcdA = arrayGCD(arrayA)
    gcdB = arrayGCD(arrayB)
    
    checkA, checkB = 0, 0
    if any(arrayA[i] % gcdB == 0 for i in range(len(arrayA))):
        checkA = 1
        
    if any(arrayB[i] % gcdA == 0 for i in range(len(arrayB))):
        checkB = 1

    return 0 if checkA == 1 and checkB == 1 else max(gcdA, gcdB)