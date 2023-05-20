from collections import deque
def solution(n, computers):
    # 인접 리스트 생성 및 초기화
    network = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and computers[i-1][j-1] == 1:
                network[i].append(j)

    cnt = 0
    check = [False]*(n+1)
    dq = deque()
    for i in range(1, n+1):
        if not len(network[i]): # 고립된 노드는 그 자체로 네트워크 망 1개를 구성
            cnt += 1
        
        elif not check[i] and len(network[i]): # 인접한 노드들을 하나의 네트워크 망으로 연결
            dq.append(i)
            check[i] = True
            cnt += 1
            while dq:
                now = dq.popleft()
                for w in network[now]:
                    if not check[w]:        
                        dq.append(w)
                        check[w] = True
    return cnt