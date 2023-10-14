from collections import deque
def solution(menu, order, k):
    dq = deque() # (손님의 입장시간, 퇴장시간)
    maxCnt = 1
    
    for i, menuIdx in enumerate(order):
        if i == 0: out = 0
        else: out = max(dq[i-1][1], i*k) # 앞 손님이 음료를 받고 나가는 시간과 다음 손님이 입장하는 시간 중 더 큰 시간 기준으로 out 시간을 계산함
        time = menu[menuIdx]
        dq.append((i*k, out+time))
    # print(dq)
    
    waiting = deque() # 대기손님
    out = dq[0][1] # 맨처음 손님이 음료를 받고 나가는 시간
    for i in range(1, len(dq)):
        if out > dq[i][0]: # 지금 만들고 있는 음료가 완성되는 시간(out) 내에 카페에 들어와있는 손님을 waiting 배열에 담음
            waiting.append(dq[i])
        else: # 지금 만들고 있는 음료가 완성되는 시간 이후에 입장하는 손님의 경우, 현재까지 대기중인 손님의 최대 수를 갱신한 뒤에 waiting 배열에 담음
            maxCnt = max(maxCnt, len(waiting)+1)
            waiting.append(dq[i]) 
            enter, out = waiting.popleft() # 다음 손님이 음료를 받고 나가는 시간으로 out을 갱신
            # print(waiting, maxCnt)
            
    maxCnt = max(maxCnt, len(waiting)+1)
    return maxCnt