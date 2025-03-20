from itertools import chain
from collections import deque
def solution(storage, requests):
    row, col = len(storage), len(storage[0])
    # 그래프 테두리(외곽영역)는 '0'요소를 가지도록 추가
    graph = [['0']*(col+2)] + [list("0"+str+"0") for str in storage]+ [['0']*(col+2)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # 외곽 영역인지 check하는 함수
    def check_outside(x, y):
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < row + 2 and 0 <= y_ < col + 2:
                if graph[x_][y_] == '0':
                    return True
        return False
    
    def bfs(target, remove_list):
        dq = deque()
        visited = [[False]*(col+2) for _ in range(row+2)]
        visited[0][0] = True
        dq.append((0, 0)) # 시작 노드는 (0, 0)
        
        while dq:
            x, y = dq.popleft()
            
            for i in range(4):
                x_ = x + dx[i]
                y_ = y + dy[i]
                if 0 <= x_ < row + 2 and 0 <= y_ < col + 2 and not visited[x_][y_]:
                    if  graph[x_][y_] == '0': # 외곽부분과 연결된 위치는 방문처리 후 dq에 넣음
                        visited[x_][y_] = True
                        dq.append((x_, y_))
                    
                    # 외곽 영역과 연결되면서 다음 노드가 타겟노드인 경우, bfs 끝나고 해당 노드 값에 '0'으로 설정하기 위해 remove_list에 추가
                    # 해당 노드는 다음 요청때 외곽 영역이 됨
                    elif graph[x_][y_] == target and check_outside(x_, y_): 
                        remove_list.append((x_, y_))
        
        # 타겟 노드(요청 컨테이너)를 외곽영역으로 표시
        for x, y in remove_list:
            graph[x][y] = '0'

    for str in requests:
        remove_list = [] 
        if len(str) > 1: # 크레인 요청
            target = str[0]
            bfs(target, remove_list)
            graph = [['0' if char == target else char for char in row] for row in graph]
        else: # 지게차 요청
            bfs(str, remove_list) 
        
    sentence = "".join(char for char in chain(*graph) if char != "0") # 0은 외곽영역이므로 이 노드 제외한 나머지 노드의 수를 구함
    return len(sentence)