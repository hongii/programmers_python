from collections import deque
def bfs(x, cutNode, visited):
    global tree
    dq = deque()
    cnt = 1
    visited[x] = True
    dq.append(x)
    # print(x, dq)
    while dq:
        y = dq.popleft()
        for k in tree[y]:
            if k != cutNode and not visited[k]:
                cnt += 1
                visited[k] = True
                dq.append(k)
                
    return cnt        
    
def solution(n, wires):
    global tree
    tree = [[] for _ in range(n+1)]
    res = n

    # 연결리스트 만들기
    for site in wires:
        x, y = site[0], site[1]
        tree[x].append(y)
        tree[y].append(x)
    print(tree)
    
    for a, b in wires:
        visited = [False for _ in range(n+1)]
        top1 = bfs(a, b, visited)
        top2 = n - top1
        if res > abs(top1-top2):
            res = abs(top1-top2)
        print(top1, top2, res)
    return res