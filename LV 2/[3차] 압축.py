# 2회차 코드 -> 시간 절약
def solution(msg):
    dic = {chr(key):key-ord("A")+1 for key in range(ord("A"), ord("Z")+1)}
    res = []
    nextVal = 27
    while msg:
        i = 0
        while i < len(msg) and msg[:i+1] in dic.keys():
            i += 1
        if msg[:i+1] not in dic.keys():
            dic[msg[:i+1]] = nextVal
        res.append(dic[msg[:i]])
        nextVal += 1
        msg = msg[i:]
    return res


# 1회차 코드 -> 시간 오래 걸림
import re
def solution(msg):
    dic = {chr(ord("A")+i-1):i for i in range(1, 27)}
    idx = []
    num = 27
    while msg:
        for k in sorted(dic.keys(), key=lambda x:len(x), reverse=True):
            if re.match(k, msg):
                if msg[:len(k)+1] not in dic.keys():
                    dic[msg[:len(k)+1]] = num
                    num += 1
                msg = msg[len(k):]
                idx.append(dic[k])
                break
    return idx
