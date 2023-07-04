#  두번째 코드 -> 다익스트라, 해시
# 참고한 풀이 사이트 - https://blog.yjyoon.dev/kakao/2022/09/17/kakao-2022-intern-04/
# 테케 25번 시간초과 해결 방법 -> 산봉우리 배열을 리스트가 아닌 해시로 사용해라 -> 파이썬의 경우, dict 또는 set이용 
# 다익스트라 함수에서 해당 노드가 산봉우리라면 continue 하는 부분에서 산봉우리 summits을 리스트로 구현하게 되면, O(n)의 시간이 걸리게 된다.
# 하지만, dict나 set을 이용하게 되면, 해당 노드가 summits에 포함되어있는지 아닌지 판별하는 데에 O(1)의 시간 밖에 안걸린다.
# list, dict, set의 시간 복잡도 참고 사이트 - https://velog.io/@juntree/Python-ListDictSet%EC%9D%98-%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84-Big-O
import heapq
def solution(n, paths, gates, summits):
    intensity = [float('inf')] * (n+1)
    graph = [[] for _ in range(n+1)]
    for x, y, w in paths:
        graph[x].append((y,w))
        graph[y].append((x,w))
    
    def Dijkstra():
        hq = []
        for x in gates:
            intensity[x] = 0
            heapq.heappush(hq,(0, x))
        
        while hq:
            d, v = heapq.heappop(hq)
            
            if d > intensity[v] or v in summits: # 시간을 줄이기 위해 summits을 set으로 바꿔서 포함관계를 탐색한다. O(1)의 수행시간으로 만들어줌
                continue
            
            for u, w in graph[v]:
                # 현재 v노드의 intensity[v]와 다음 노드(u)의 가중치(w) 중 더 큰 값으로 intensity 갱신(하나의 경로 내에선 최대 가중치가 그 경로의 intensity가 된다.
                new_intensity = max(intensity[v], w)
                if intensity[u] > new_intensity: # 여러 경로들 비교할땐, 해당 노드로 가능 최소 가중치가 intensity가 된다. 따라서, 최소 intensity가 생기는 경로일때만 hq에 넣음
                    intensity[u] = new_intensity
                    heapq.heappush(hq, (new_intensity, u))

    
    summits = set(summits) # 수행시간 줄이기 위함
    Dijkstra() 
    minIntensity, minSummit = float('inf'), 0
    for v in sorted(list(summits)):
        if minIntensity > intensity[v]:
            minIntensity = intensity[v]
            minSummit = v
    return [minSummit, minIntensity]
        



''' 첫번째 코드 -> dfs 이용, 드러운 코드. 예제 통과, 5개 제외한 테케 런에러 및 시간초과
def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for x in paths:
        graph[x[0]].append((x[1],x[2]))
        graph[x[1]].append((x[0],x[2]))
    
    def dfs(s, e, it, gateTmp, summitsTmp):
        global visited, tmp
        if s == e:
            tmp.append(it)
            return
        
        for x in graph[s]:
            u, w = x[0], x[1]
            if not visited[u] and u not in gateTmp and u not in summitsTmp:
                visited[u] = True
                
                if w > it:
                    dfs(u, e, w, gateTmp, summitsTmp)
                else:
                    dfs(u, e, it, gateTmp, summitsTmp)
                
                visited[u] = False
        
    
    intensityMin = 10e9
    for i in range(len(gates)):
        for j in range(len(summits)):
            global visited, tmp
            tmp = []
            visited = [False]*(n+1)
            visited[gates[i]] = True
            tmpSum = summits.copy()
            tmpSum.remove(summits[j])
            dfs(gates[i], summits[j], 0, gates, tmpSum)
            intensity = min(tmp)
            
            tmp = []
            tmpGate = gates.copy()
            tmpGate.remove(gates[i])
            visited = [False]*(n+1)
            visited[summits[j]] = True
            
            dfs(summits[j], gates[i], 0, summits, tmpGate)
            intensity = min(min(tmp), intensity)
            
            if intensity < intensityMin:
                intensityMin = intensity
                end = summits[j]
            elif intensity == intensityMin:
                end = min(end, summits[j])
            
    return [end, intensityMin]
'''