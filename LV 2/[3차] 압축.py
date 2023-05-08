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
