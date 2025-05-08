# 그리디 알고리즘
def solution(targets):
    targets.sort(key=lambda x:x[1]) # 정렬
    
    last_x = -1
    cnt = 0
    for s, e in targets: # 탐색
        if last_x <= s:
            cnt += 1
            last_x = e
    
    return cnt