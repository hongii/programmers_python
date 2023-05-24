# 다시 풀어볼 문제
# 스케줄러(운영체제 SFJ 스케줄링-최소 작업 우선 스케줄링), 풀이 완벽 이해 못함
import heapq
def solution(jobs):
    hq = [] # 작업 소요시간이 낮은 순으로 최소힙 구성
    jobs.sort()
    res, now, i = 0, 0, 0
    start = -1
    while i < len(jobs):
        # 현재 시점(now)에서 처리 가능한 작업들 선별
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(hq, (job[1], job[0])) # (작업 소요시간, 요청시점)

        if hq:
            time, requireTime = heapq.heappop(hq)
            start = now
            now += time
            res += now - requireTime
            i += 1
        else:
            now += 1
    return res // i