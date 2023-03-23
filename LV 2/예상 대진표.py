import math
def solution(n,a,b):
    match = 0
    cnt = int(math.log2(n))
    if a > b:
        a, b = b, a

    for i in range(cnt):
        match += 1
        if a == b-1 and math.ceil(a/2) == math.ceil(b/2):
            break  
        a, b = math.ceil(a/2), math.ceil(b/2)

    return match