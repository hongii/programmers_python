from itertools import combinations_with_replacement
def solution(n, info):
    case = combinations_with_replacement(range(11), n)
    sub = []

    for c in case:
        res = [0]*11
        for score in c:
            res[score] += 1

        ryan, apeach = 0, 0
        for i in range(11):
            if info[i] < res[i] and res[i] != 0:
                ryan += 10 - i
            elif info[i] >= res[i] and info[i] != 0:
                apeach += 10 - i

        if ryan > apeach:
            sub.append([ryan - apeach, res])

    if len(sub) == 0:
        return [-1]

    sub.sort(reverse=True)
    ans = sub[0]
    for i in range(1, len(sub)):
        if sub[0][0] == sub[i][0]:
            cmp = sub[i][1]
            for j in range(10, -1, -1):
                if ans[1][j] < cmp[j]:
                    ans[1] = cmp
                    break
        else:
            break

    return ans[1]
  
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))