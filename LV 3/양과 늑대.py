# 풀이 참고한 사이트 - https://blog.encrypted.gg/1029
# 비트마스킹 참고한 사이트 - https://travelbeeee.tistory.com/451, https://rebro.kr/63
# dfs(또는 bfs)와 비트마스킹
def solution(info, edges):
  global sheap
  sheap = 1
  left = [-1] * len(info) # 각 노드들의 왼쪽 자식 노드를 저장
  right = [-1] * len(info) # 각 노드들의 오른쪽 자식 노드를 저장
  visited = [False] * (1 << len(info))
  for v, u in edges: # v = 부모노드, u = 자식노드
    if left[v] == -1: # 일단 먼저 등장한 자식 노드부터 왼쪽 자식에 배치
      left[v] = u
    else: # 만약 이미 왼쪽 자식노드가 있다면, 현재 자식노드를 부모노드의 오른쪽 자식 노드로 배치
      right[v] = u

  def dfs(state, info): # state는 가능한 경로의 부분집합을 비트마스크로 대응시킨 값. 
                        # ex) 0번->1번->4번 노드를 경유하는 경우, 집합 {0, 1, 4}를 비트 마스크로 표현하면 10011(2)이다. 이를 10진수 값으로 바꾸면 19가 되므로, state = 19가 된다.
    global sheap
    if visited[state]:
      return
    
    visited[state] = True
    wolf, nodeCnt = 0, 0 # 늑대의 수, 전체 정점의 수

    # 비트마스크를 이용하여 현재 경로(state)의 양의 갯수를 모두 비교한다.
    for i in range(len(info)):
      if state & (1<<i): # state에 i번 노드가 포함되는지 확인(원소의 포함관계 확인). 
        nodeCnt += 1 # 양이 있는 노드와 늑대가 있는 노드 총 갯수를 저장
        wolf += info[i] # 현재 state는 i번 노드를 거쳐가는 경로이므로, info리스트의 index i에 해당하는 값을 더한다.
                        # (info는 양인 경우엔 0, 늑대인 경우엔 1이므로 어짜피 현재 i번 노드가 양인 경우엔 0이 더해지므로, 늑대 수에 더하고 난 후 나중에 nodeCnt값에서 wolf를 뺀 값은 양의 갯수가 된다) 

    # 만약 늑대가 현재 지나온 노드 중에 절반 이상에 해당 되는 경우엔 갈 수 없는 경로이므로 종료.
    if wolf*2 >= nodeCnt: 
      return
    sheap = max(sheap, nodeCnt-wolf)

    # 갈 수 있는 경로 (다음 state) 구하기 -> 0~len(info)번 node를 통해 갈 수 있는 부분집합 구하기
    # 현재 state를 포함하는 경로여야함(ex. state가 9라면, 1001(2)이므로, 현재 0번-> 3번 노드를 거쳐온 경로라는 뜻. 그러므로 다음 state는 이 0번과 3번 노드를 포함한 경로여야 한다.)
    for i in range(len(info)):
      if not state & (1<<i): # 현재 state에 포함되지 않는 노드는 pass. 
        continue
      if left[i] != -1: # 현재 state에 포함되는 노드 중에서 왼쪽 자식 또는 오른쪽자식이 존재한다면 다음 state에 추가하여 dfs수행
        dfs(state | (1<<left[i]), info)
      if right[i] != -1:
        dfs(state | (1<<right[i]), info)

  dfs(1)
  return sheap