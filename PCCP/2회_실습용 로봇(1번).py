def solution(command):
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]; # 로봇 방향 -> 상, 우, 하, 좌 (시계방향)
    robot = [0, 0, 0] # [x, y, 로봇 방향 index] 
    
    for c in command:
        if c == "R":
            robot[2] = (robot[2]+1)%4 # 시계방향 90도 회전  
        elif c == "L":
            robot[2] = (robot[2]+3)%4 # 반시계방향 90도 회전
        elif c == "G":
            dx, dy = direct[robot[2]]
            robot[0] += dx
            robot[1] += dy
        elif c == "B":
            dx, dy = direct[robot[2]]
            robot[0] -= dx
            robot[1] -= dy
    return [robot[0], robot[1]]
