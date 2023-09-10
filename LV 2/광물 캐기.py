# 첫번째 코드 -> 33번 35번에서 시간초과, 순열구해서 풀었음(완탐)
import math
from itertools import permutations
def solution(picks, minerals):
    dic_idx = {"diamond":0, "iron":1, "stone":2}
    dic = {"diamond":[1, 1, 1], "iron":[5, 1, 1], "stone":[25, 5, 1]}

    tmp = []
    for i, pick in enumerate(dic.keys()):
        for _ in range(picks[i]):
            tmp.append(pick)
    
    total = sum(picks) * 5
    pm_cnt = min(total, len(minerals))
    pm = set(permutations(tmp, math.ceil(pm_cnt/5)))
    
    minFatigue = 10e6
    for p in pm:
        fatigue, i = 0, 0
        for x in p:
            cnt = 0
            while len(minerals) > i and cnt < 5:
                idx = dic_idx[minerals[i]]
                fatigue += dic[x][idx]
                cnt += 1
                i += 1
        minFatigue = min(fatigue, minFatigue)
    return minFatigue


# 두번째 코드 -> 모든 테케 0.02ms ~ 0.07ms로 통과
# 광물을 캐는 순서가 있다. 문제에서 주어진 순서대로만 광물을 캘 수 있다. -> 완전 탐색이 아니라 그리디로 풀 수 있음. (만약 광물 캐는 순서가 없었다면 완탐으로 풀어야 했을 것)
# 광물을 캘 때 필요한 피로도의 가중치가 존재함 -> 다이아 > 철 > 스톤 순으로 가중치가 매겨진다. 
# 참고로, 다이아 곡괭이로 광물을 캘때는 피로도 가중치가 1로 모두 동일하다. 
# 또한, 철 곡괭이로 다이아 광물을 캘땐 피로도 5, 나머지 광물은 1로 동일하다. 
# 마지막으로 스톤 곡괭이로 광물을 캘 땐 다이아 25, 철 5, 스톤 1로 확실하게 가중치가 나뉘어져 있다.
# 따라서, 그리디로 접근하는 것이 가능하고, 5개 광물을 캘 때 필요한 총 피로도 계산은 스톤 곡괭이로 캤을 때로 구하면 된다.
# 이렇게 광물 5개씩 묶어서 스톤 곡괭이로 캤을 때 필요한 총 피로도를 내림차순으로 정렬하고, 가장 피로도 많이 필요한 것 부터 다이아 -> 철-> 스톤 곡괭이를 소모하도록 한다. 
# 즉, 광물 5세트씩 스톤 곡괭이로 캤을때 필요한 피로도 기준으로 내림차순 정렬을 하고, 
# 이렇게 정렬된 가장 피로도가 큰 스톤셋부터 다이아 곡괭이부터 모두 소진하고 그 다음 철, 마지막으로 스톤곡괭이로 캤을 때 필요한 총 피로도를 계산하면 최소 피로도가 구해진다.
import math
def solution(picks, minerals):
    if not sum(picks):
        return 0

    fig_idx = {"diamond":0, "iron":1, "stone":2}
    pick_fig = {"diamond":[1, 1, 1], "iron":[5, 1, 1], "stone":[25, 5, 1]}
    tmp = []
    for i, pick in enumerate(pick_fig.keys()):
        for _ in range(picks[i]):
            tmp.append(pick)

    fiveFatigue = []
    idx = 0
    for i in range(math.ceil(len(minerals)/5)):
        cnt, f = 0, 0
        while cnt < 5 and idx < len(minerals):
            f += pick_fig["stone"][fig_idx[minerals[idx]]]
            cnt += 1
            idx += 1
        if idx % 5 != 0:
            fiveFatigue.append((f, minerals[idx-(idx%5):idx]))
        else:
            fiveFatigue.append((f, minerals[idx-5:idx]))

        if len(fiveFatigue) == sum(picks):
            break

    fiveFatigue.sort(key=lambda x:x[0], reverse=True)
    fatigue = 0
    for i, (_, fiveMinerals) in enumerate(fiveFatigue):
        for x in fiveMinerals:
            pick = tmp[i]
            fatigue += pick_fig[pick][fig_idx[x]]
    return fatigue