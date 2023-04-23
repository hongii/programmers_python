import itertools
def solution(n):
    snail = [[0]*i for i in range(1, n+1)]
    num, cnt, mode = 1, n, 1
    x, y = 0, 0

    for i in range(1, n+1):
        if mode%3 == 1: # 아래방향
            for _ in range(cnt):    
                snail[x][y] = num
                x += 1
                num += 1
            x -= 1
            y += 1

        elif mode%3 == 2: # 가로방향
            for _ in range(cnt):
                snail[x][y] = num
                num += 1
                y += 1
            x -= 1
            y -= 2

        elif mode%3 == 0: # 왼쪽위 대각선방향
            for _ in range(cnt):
                snail[x][y] = num
                num += 1
                x -= 1
                y -= 1
            x += 2
            y += 1

        mode += 1
        cnt -= 1
    return list(itertools.chain(*snail))

'''
# 2차원 리스트를 1차원 리스트로 바꾸는 방법
1. itertools로 2차원 -> 1차원 리스트 변환
  => list(itertools.chain(*snail))
1-1) itertools.chain.from_iterable()를 사용하면 *를 입력하지 않고 바로 인자를 전달할 수 있다
  => list(itertools.chain.from_iterable(snail))

2. sum()으로 2차원 리스트를 1차원 리스트로 변환
  => snail_1 = sum(snail, [])
'''