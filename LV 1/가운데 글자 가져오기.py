def solution(s):
    centerStr = len(s)//2
    if len(s) % 2 == 0:
        return s[centerStr - 1:centerStr + 1]
    return s[centerStr]