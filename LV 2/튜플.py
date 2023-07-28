# 2회차 코드
def solution(s):
    s = s[2:-2]
    s = s.split("},{")
    tmp = []
    for x in s:
        x = x.split(",")
        tmp.append(set(x))
    tmp.sort(key=lambda x:len(x))
    
    res = [int(*tmp[0])]
    for i in range(1, len(tmp)):
        nextNum = tmp[i] - tmp[i-1] 
        res.append(int(*nextNum))
    return res


# 1회차 코드
def solution(s):
    s = s[2:-2]
    l = s.split("},{")
    res = []
    for x in l:
        tmp = x.split(",")
        res.append(tmp)
    res.sort(key=lambda x:len(x))

    l1 = res[0]
    for i in range(1, len(res)):
        l2 = res[i]
        num = list(set(l2) - set(l1))
        l1.extend(num)
    return [int(n) for n in l1]


''' 첫번째 풀이 pass -> split 제대로 못해서 반복문 사용하여 문자열 구분시도
def solution(s):
    s = s[1:-1]
    tmpL, l = [], []
    num, check = "", 0
    for i in range(len(s)):
        if s[i] == "{":
            check = 1
        elif s[i] == "," and check == 1:
            tmpL.append(num)
            num = ""
        elif s[i] == "}":
            tmpL.append(num)
            l.append(tmpL)
            check = 0
            num = ""
            tmpL = []
        elif s[i].isdecimal():
            num += s[i]
    l.sort(key=lambda x:len(x))
    
    l1 = l[0]
    for i in range(1, len(l)):
        l2 = l[i]
        num = list(set(l2) - set(l1))
        l1.extend(num)
    return [int(n) for n in l1]
'''