def solution(routes):
    routes.sort(key=lambda x:x[1])
    camera = -30001
    cnt = 0
    for i in range(len(routes)):
        if routes[i][0] > camera:
            camera = routes[i][1]
            cnt += 1
    return cnt

'''
# 문제 플이
=> 진출지점 기준으로 오름차순으로 정렬, 카메라는 먼저 진출한지점 순서대로 설치되어야한다.
  만약 차량의 진입위치가 설치된 카메라보다 앞이라면, 카메라를 지나치므로 카메라의 추가적인 설치가 필요없다.
  즉, 진입 위치가 마지막으로 설치된 카메라의 위치보다 뒤라면, 추가적인 카메라 설치가 필요하며 이 때 마지막으로 설치된 카메라의 위치는 해당 차량의 진출구간으로 갱신한다.
'''