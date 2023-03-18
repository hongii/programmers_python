from collections import Counter
def solution(id_list, report, k):
    answer = []
    declare_user = []
    user_declareUser = {}
    declare_cnt = {}

    for ID in id_list:
        if ID not in user_declareUser.keys():
            user_declareUser[ID] = []

    for users in report:
        user, declaredUser = map(str, users.split())
        if declaredUser not in user_declareUser[user]:
            user_declareUser[user].append(declaredUser)
            if declaredUser not in declare_cnt.keys():
                declare_cnt[declaredUser] = 1
            else:
                declare_cnt[declaredUser] += 1

    for key, value in declare_cnt.items():
        if value >= k:
            declare_user.append(key)

    for name in id_list:
        cnt = 0
        for dUser in declare_user:
            if dUser in user_declareUser[name]:
                cnt += 1
        answer.append(cnt)

    return answer

'''최적의 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list} # x가 신고당한 횟수를 저장할 dic

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k: # 해당 유저의 신고당한 횟수가 k이상이라면
            # answer[id_list.index(r.split()[0])] += 1  # 해당 유저를 신고한 유저의 idx를 id_list에서 찾아서, 신고결과 메일 받는 횟수를 +1 한다.

    return answer
'''
# 필요한 정보만 쏙쏙 골라서 푸는 스킬 키우자..