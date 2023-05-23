from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for site in edge:
        graph[site[0]].append(site[1])
        graph[site[1]].append(site[0])

    dq = deque()
    visited = [False]*(n+1)
    distance = [0]*(n+1)
    visited[1] = True
    dq.append(1)
    while dq:
        now = dq.popleft()
        visited[now] = True
        for x in graph[now]:
            if not visited[x]:
                visited[x] = True
                dq.append(x)
                distance[x] = distance[now] + 1

    maxDistance = max(distance)
    cnt = 0
    for i in range(1, n+1):
        if maxDistance == distance[i]:
            cnt += 1
    return cnt