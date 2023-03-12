def solution(s):
    res = []
    dict = {}
    for i in range(len(s)):
        if s.find(s[i], 0, i) == -1:
            res.append(-1)
        else:
            res.append(i - dict[s[i]])
        dict[s[i]] = i
    return res

'''최적의 풀이
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer

'''