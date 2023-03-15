def solution(X, Y):
    listX, listY = list(X), list(Y)
    intersection = list(set(listX) & set(listY))
    if len(intersection) == 0:
        return "-1"
    elif intersection == ['0']:
        return "0"
    else:
        res = intersection
        for i in range(len(intersection)):
            cntX = listX.count(intersection[i])
            cntY = listY.count(intersection[i])
            if cntX != cntY or (cntX > 1 and cntY > 1):
                addCnt = min(cntX, cntY) -1
                for j in range(addCnt):
                    res.append(intersection[i])
        res.sort(reverse=True)
        return "".join(res)

''' 최적의 풀이
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
'''