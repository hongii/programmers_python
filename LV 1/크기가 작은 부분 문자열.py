def solution(t, p):
    last = len(p) - 1
    cnt = 0
    for i in range(len(t)):
        if last == len(t):
            break
        if int(p) >= int(t[i:last+1]):
            cnt += 1
        last += 1
    return cnt