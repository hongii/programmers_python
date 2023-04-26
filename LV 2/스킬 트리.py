def solution(skill, skill_trees):
    res = 0
    for skillTree in skill_trees:
        i, flag = 0, 0
        check = [27]*len(skill)
        for s in skillTree:
            if s in skill:
                if skill[i] != s:
                    flag = -1
                    break
                elif i < len(skill) and skill[i] == s:
                    check[i] = i+1
                    i += 1

        if flag != -1 and sorted(check) == check:
            res += 1
    return res

'''더 깔끔한 다른 사람 풀이
def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer

'''