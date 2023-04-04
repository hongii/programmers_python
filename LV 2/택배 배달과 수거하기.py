def solution(cap, n, deliveries, pickups):
    dCnt, pCnt, dist = 0, 0, 0
    dp, pp = n-1, n-1 # dp: deliveries pointer, pp: pickups pointer

    if sum(deliveries) == 0 and sum(pickups) == 0:
        return dist

    while dp >= 0 or pp >= 0:
        dist += max((dp+1) * 2, (pp+1) * 2) 

        while dCnt < cap and dp >= 0:
            dCnt += deliveries[dp]
            dp -= 1
            if dCnt > cap:
                dp += 1
                dCnt -= deliveries[dp]
                gap = cap - dCnt
                deliveries[dp] -= gap 
                dCnt = 0
                break
            elif dCnt == cap:
                dCnt = 0
                break

        while pCnt < cap and pp >= 0:
            pCnt += pickups[pp]
            pp -= 1
            if pCnt > cap:
                pp += 1
                pCnt -= pickups[pp]
                gap = cap - pCnt
                pickups[pp] -= gap 
                pCnt = 0
                break
            elif pCnt == cap:
                pCnt = 0
                break

        while dp >= 0 and deliveries[dp] == 0:
            dp -= 1
        while pp >= 0 and pickups[pp] == 0:
            pp -= 1
    return dist

'''
좀 더 간결한 코드의 그리디 활용법
def solution(cap, n, deliveries, pickups):
    dist = 0
    d, p = 0, 0
    for i in range(n-1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        while d > 0 or p > 0:
            d -= cap
            p -= cap
            dist += (i + 1) * 2 

    return dist

=> 가장 먼 곳 부터 탐색. 배달할 상자가 있거나(or) 칙업해야할 상자가 하나라도 있다면 그 곳까지 가야한다.(dist 추가)
=> 먼저 리스트 맨 뒤 부터 탐색하면서 배달할 상자(d)와 픽업할 상자(p)를 각각 더해준다. (line 51~ 52)
=> 배달할 상자 또는 픽업할 상자가 하나라도 있다면(양수라면) cap 만큼 빼준다 -> d와 p가 모두 음수값이 된다면 한번 왕복 움직일 때 여러집에 배달 및 픽업이 가능하다는 뜻 
=> 따라서, d또는 p 값이 양수일때만 cap만큼 빼주고 dist를 더해주면 된다.
'''