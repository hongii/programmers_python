import heapq
def Dijkstra(start, N):
    global graph, dist
    hq = []
    dist = [500001] * (N+1)
    heapq.heappush(hq, (0, start)) # (거리, 노드)형태로 최소힙 구현
    dist[start] = 0 # 시작 노드의 자기 자신까지의 거리는 0으로 초기화
    while hq:
        d, node = heapq.heappop(hq)

        # 이미 최단거리가 구해진(방문처리가 끝난) 마을(node)는 pass
        if dist[node] < d:
            continue

        for g in graph[node]:
            u, w = g[0], g[1]
            if d + w < dist[u]: # 현재노드(node)에서 인접한 노드(u)까지의 최단거리 갱신
                dist[u] = d + w
                heapq.heappush(hq, (d+w, u)) # 최단거리가 갱신된 노드들만 최소힙에 넣어줌

def solution(N, road, K):
    global graph, dist
    graph = [[] for _ in range(N+1)]
    for v, u, w in road:
        graph[v].append([u, w])
        graph[u].append([v, w])

    Dijkstra(1, N)
    cnt = 0
    for d in dist:
        if d <= K:
            cnt += 1
    return cnt