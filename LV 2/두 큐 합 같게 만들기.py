from collections import deque
def solution(queue1, queue2):
    res = 0
    dq1, dq2 = deque(queue1), deque(queue2)
    tmp1, tmp2 = dq1, dq2
    sum1, sum2 = sum(dq1), sum(dq2)

    if (sum1+sum2) % 2 != 0:
        return -1

    while sum1 != sum2:
        if len(dq1) == 0 or len(dq2) == 0:
            res = -1
            break
        # res>len(queue1)*4 는 테케 11, 테케 28에 대한 반례 queue1 = [1, 4] queue2 = [3, 4]에 대한 조건 
        # 즉, 만족하는 답이 없이 계속 로테이션 도는 경우 (위의 반례에선 8회 수행한 경우(res = 8), dq1와 dq2는 각각 원래의 queue1과 queue2와 동일한 값으로 돌아온다.) 
        elif res > len(queue1)*4 and dq1 == tmp1 and dq2 == tmp2:
            res = -1
            break
        elif sum1 > sum2:
            num = dq1.popleft()
            dq2.append(num)
            sum1 -= num
            sum2 += dq2[-1]
        elif sum1 < sum2:
            num = dq2.popleft()
            dq1.append(num)
            sum2 -= num
            sum1 += dq1[-1]
        res += 1

    return res
