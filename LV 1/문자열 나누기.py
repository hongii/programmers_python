def solution(s):
    first = s[0]
    same, dif = 0, 0
    subStrCnt = 0
    length = len(s)
    for i in range(length):
        if first == s[i]:
            same += 1
        else:
            dif += 1

        if same == dif:
            same, dif = 0, 0
            subStrCnt += 1
            if i+1 < length - 1:
                first = s[i+1]      
        elif i == length -1:
            subStrCnt += 1

    return subStrCnt