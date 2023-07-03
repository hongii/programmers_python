from collections import deque
def solution(n, m, x, y, r, c, k):
  dx = [1, 0, 0, -1] # 사전순으로 배치 -> d, l, r, u
  dy = [0, -1, 1, 0]
  direction = {0: "d", 1: "l", 2: "r", 3: "u"}
  dq = deque()
  dq.append((x, y, 0, "")) # (x좌표, y좌표, 거리, 경로)

  while dq:
    i, j, d, p = dq.popleft()
    if (i, j) == (r, c) and (k-d)%2 == 1: # 왕복으로 도착지점에 되돌아 올 수 없는 경우
      return "impossible" 

    if (i, j) == (r, c) and d == k:
      return p

    for a in range(4): # 사전순 방향으로 순회
      x_ = i + dx[a]
      y_ = j + dy[a]
      if 0 < x_ <= n and 0 < y_ <= m:
        if abs(r-x_) + abs(c-y_) + d+1 <= k:
          dq.append((x_, y_, d+1, p+direction[a]))
          break # 사전순으로 순회하므로 이미 조건문을 통과한 경로가 있다면 남은 방향은 확인할 필요 없음

  return "impossible"


'''
# 다른 사람 풀이 참고
bfs로 풀었는데 시간초과에서 벗어나기 위한 추가적인 조건이 필요함
추가 조건 1) if (i, j) == (r, c) and (k-d)%2 == 1 
-> 현재 위치가 도착지점인데 도착지점에서 벗어났다가 다시 되돌아 오는 횟수는 짝수여야 하므로(왔다 갔다) 남은 거리가 홀수인 경우, k횟수만에 도착지점에 도달 불가능하므로 "impossible" 
추가 조건 2) dx와 dy를 사전순으로 배치 & if abs(r-x_) + abs(c-y_) + d+1 <= k: 조건 추가
-> 조건에 의해 현재 거리(d+1)와 도착 지점까지 남은 거리(abs(r-x_) + abs(c-y_))의 합이 k번 이하인 경우에만 다음 위치로 이동. 
    이 조건을 만족한 경로는 사전순으로 가장 빠른 경로만 찾을 것이기 떄문에 break로 나머지 방향은 확인 안해도 됨

if abs(r-x_) + abs(c-y_) + d+1 <= k:
  dq.append((x_, y_, d+1, p+direction[a]))
  break
위의 코드를 통해, 거리가 1씩 증가할 때 마다 각 경로의 사전 순으로 가장 빠른 방향만 check 
ex) 출발 좌표(2, 3), 도착 죄표(3, 1) -> 1번째 경로 : "d"
                                      2번째 경로 : "dl"
                                      3번째 경로 : "dll"
                                      4번째 경로 : "dllr"
                                      5번째 경로 : "dllrl" -> 도착 지점에 k번(5번)만에 도달했으므로 가장 사전순으로 가장 빠른 경로는 "dllrl"이다.
'''