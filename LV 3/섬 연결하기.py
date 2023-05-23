# 첫번째는 다익스트라로 구현했으나, 다익스트라는 출발 노드로 부터 다른 모든 노드까지의 최소 비용을 구하는 것이므로 적절하지 않다는 것을 깨달음..
# 즉, 다익스트라는 1->3번 노드로 가는 최소비용, 1->4번 노드로 가는 최소비용 등과 같이 정해진 출발 노드로 부터 다른 노드까지의 최소비용을 알려주는 알고리즘이다.
# 따라서, 크루스칼 알고리즘 또는 프림 알고리즘을 이용하여야 한다. -> 최소 신장 트리 알고리즘 문제 유형(모든 노드가 연결된 경로의 총 비용이 최소인 경로를 찾기)
# 크루스칼 알고리즘과 프림 알고리즘, 다익스트라 알고리즘은 그리디 알고리즘을 적용하는 알고리즘이다.

# 크루스칼 알고리즘을 이용한 두번째 코드 
def find_root(x):
    global parent
    if parent[x] != x:
        parent[x] = find_root(parent[x])
    return parent[x]

def union_node(a, b):
    global parent
    root_a = find_root(a)
    root_b = find_root(b)
    if root_a > root_b:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a

def solution(n, costs):
    res = 0
    costs.sort(key=lambda x:x[2])
    global parent
    parent = [i for i in range(n)]

    for x in costs:
        v, w, cost = x[0], x[1], x[2]
        if find_root(v) != find_root(w):
            union_node(v, w)
            res += cost
            # print(v, w, cost)
    return res

'''
# 첫번째 코드 -> 인접리스트 이용한 다익스트라 구현
import heapq
def solution(n, costs):
    distance = [10e9]*n
    graph = [[]*n for _ in range(n)]
    for x in costs:
        graph[x[0]].append([x[1], x[2]])
        graph[x[1]].append([x[0], x[2]])

    distance[0] = 0
    hq = []
    heapq.heappush(hq, (0, 0)) # (거리, 노드번호)
    while hq:
        dist, now = heapq.heappop(hq)
        if dist > distance[now]: # 이미 방문처리 완료된 노드는 pass
            continue

        for x in graph[now]:
            if distance[x[0]] > dist + x[1]:
                distance[x[0]] = dist + x[1]
                heapq.heappush(hq, (distance[x[0]], x[0]))
    print(distance)
    return distance[n-1]


# 첫번째 코드 -> 그래프 이용한 다익스트라 구현
import heapq
def solution(n, costs):
    distance = [10e9]*n
    graph = [[0]*n for _ in range(n)]
    for x in costs:
        graph[x[0]][x[1]] = x[2]
        graph[x[1]][x[0]] = x[2]
    print(graph)
    distance[0] = 0
    hq = []
    heapq.heappush(hq, (0, 0)) # (거리, 노드번호)
    while hq:
        dist, now = heapq.heappop(hq)
        if dist > distance[now]: # 이미 방문처리 완료된 노드는 pass
            continue
            
        for i in range(len(graph[now])):
            if i != now and graph[now][i] != 0 and distance[i] > dist + graph[now][i]:
                print(now, i, dist,  graph[now][i])
                distance[i] = dist + graph[now][i]
                heapq.heappush(hq, (distance[i], i))
        print(hq)
    print(distance)
solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
'''