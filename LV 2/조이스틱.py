def solution(name):
    cnt = 0 # 조이스틱 총 조절 횟수
    
    # 초기의 최소 좌우이동 횟수는 'name의 길이-1'(왼쪽 -> 오른쪽으로 쭉 이동하는 경우)
    LRcnt = len(name) - 1
    
    for i, s in enumerate(name):
        # 알파벳 변경(상하 조절)
        cnt += min(ord(s)-ord('A'), ord('Z')-ord(s)+1)
        
        # 현재 알파벳의 그 다음부터 연속된 A문자열 찾기
        j = i+1 
        while j < len(name) and name[j] == "A":
            j += 1
    
        # 기존의 좌우 이동 최소횟수, 연속된 A의 왼->오 방향의 최소횟수, 연속된 A의 오->왼 방향의 최소횟수 중 최소값으로 갱신(좌우 조절)
        LRcnt = min(LRcnt, 2*i + len(name) - j, i + 2*(len(name)-j))
        
    cnt += LRcnt
    return cnt

''' 첫번째 코드 -> 틀린 풀이
def solution(name):
    cnt, cntA, idx = 0, 0, 0
    name = list(name)
    for i in range(len(name)):
        # 좌우이동(위치) 조작여부
        if name[i] == "A":
            if cntA == 0:
                idx = i-1
            cntA += 1
            continue
        elif cntA > 0 and name[i] != "A":
            if (len(name)-1) - i + idx < cntA:
                cnt += (len(name)-1) - i + idx
            else:
                cnt += cntA
            cntA, idx = 0, 0
            
        # 상하이동(알파벳) 조작
        if (ord(name[i])-ord("A")) % 26 <= 26/2:
            cnt += (ord(name[i])-ord("A")) % 26
            
        else:
            cnt += (ord("Z")-ord(name[i])) % 26 + 1
            
        cnt += 1 # 옆으로 1칸(다음 알파벳으로 이동)
        print(cnt)
    return cnt-1

'''