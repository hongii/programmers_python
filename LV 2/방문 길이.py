# 2회차 풀이
def solution(dirs):
    dis = 0
    dic = {"L":(-1, 0), "R":(1, 0), "U":(0, 1), "D":(0,-1)}
    now = (0, 0)
    s = set()
    for d in dirs:
        dx = now[0] + dic[d][0]
        dy = now[1] + dic[d][1]
        if -5 <= dx <= 5 and -5 <= dy <= 5:
            if (now, (dx, dy)) not in s:
                dis += 1
                s.add((now, (dx, dy)))
                s.add(((dx, dy), now))
            now = (dx, dy)
    return dis


# 1회차 풀이
def solution(dirs):
    dis = 0
    x, y = 5, 5
    s = set()
    d = {"L":(-1, 0), "R":(1, 0), "U":(0, 1), "D":(0,-1)}
    for k in dirs:
        dx, dy = d[k][0], d[k][1]
        size = len(s)
        if 0 <= x+dx <= 10 and 0 <= y+dy <= 10:
            # 지나가는 좌표를 양방향으로 넣어준다. 
            # 즉, (5, 5) -> (5, 6)으로 간 경우 dis += 1을 했다면, 추후 (5, 6) -> (5, 5)으로 되돌아 가는 경우에는 이미 지나간 지점이므로 dis를 더하지 앟는다.        
            s.add((x, y, x+dx, y+dy)) 
            s.add((x+dx, y+dy, x, y))
            x += dx
            y += dy
            if len(s) != size:
                dis += 1
    return dis