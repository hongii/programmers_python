def hanoi(n,start,dest,mid):
    global res
    if n == 1:
        # print('{0}번 -> {1}번 이동'.format(start, dest))
        res.append([start,dest])
    else:
        hanoi(n-1,start,mid,dest) # start기둥에서 보조 기둥으로 n-1개의 원판 이동
        # print('{0}번 -> {1}번 이동'.format(start, dest))
        res.append([start,dest]) # start 기둥에 마지막으로 남은 하나의 원판을 dest로 이동
        hanoi(n-1,mid,dest,start) # 보조기둥에서 dest기둥올 n-1개의 원판 이동

def solution(n):
    global res
    res = []
    hanoi(n,1,3,2)
    return res