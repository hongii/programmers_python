# 두번째 코드
''' 풀이 아이디어
첫번째 코드의 1번 아이디어를 개선 : 출발지 -> 목적지로 가는 최단 경로를 구하기 위해 각 출발지 노드에서 다익스트라를 매번 돌림
=> 근데 생각해보면 목적지 노드는 항상 고정이고 출발지 노드만 바뀌는 상황. 그럼 출발지와 목적지를 반대로 생각했을때, 출발지는 고정이고 목적지가 매번 바뀌는 상황
즉, 각 출발지마다 다익스트라를 매번 돌리는 것이 아니라 한번의 다익스트라로 출발지 -> 다른 노드(목적지)로 가는 최단 경로를 구할 수 있다. => 이 부분을 두번째 풀이에서 구현함

'''
import heapq


def solution(n, roads, sources, destination):
    area = [[] for _ in range(n+1)]
    for x in roads:
        a, b = x[0], x[1]
        area[a].append(b)
        area[b].append(a)

    def Dijkstra(s):
        hq = []
        distance = [float('inf')] * (n+1)
        distance[s] = 0
        heapq.heappush(hq, (0, s))
        while hq:
            dist, now = heapq.heappop(hq)
            if dist > distance[now]:
                continue

            for v in area[now]:
                if distance[v] > dist + 1:
                    distance[v] = dist+1
                    heapq.heappush(hq, (dist+1, v))
        return distance

    distance = Dijkstra(destination)
    res = [distance[s] if distance[s] != float('inf') else -1 for s in sources]
    return res


''' 첫번째 코드 -> 시간초과. 
# 풀이 아이디어
1. 각 source마다 destination로 가는 최단 경로를 구했음. 
2. 이 문제는 모든 노드 사이의 거리가 1로 동일하기 때문에 굳이 distance 배열을 사용하지 않고 visited 배열을 이용하여 방문 처리만 해줘도 된다고 생각함. 
hq에 넣을때 거리 정보를 함께 넣어주면 된다. 따라서, distance 배열 사용 안하고 visited 배열을 사용함

import heapq
def solution(n, roads, sources, destination):
    area = [[] for _ in range(n+1)] 
    for x in roads:
        a, b = x[0], x[1]
        area[a].append(b)
        area[b].append(a)
    
    def Dijkstra(s, destination):
        hq = []
        visited = [False] * (n+1)
        visited[s] = True
        heapq.heappush(hq, (0, s))
        while hq:
            dist, now = heapq.heappop(hq)

            if now == destination:
                return dist
            
            for v in area[now]:
                if not visited[v]:
                    visited[v] = True
                    heapq.heappush(hq, (dist+1, v))
        return -1
    
    
    res = []
    for s in sources:
        sdDist = Dijkstra(s, destination)
        res.append(sdDist)
    return res

'''
