# 2회차 코드
import heapq as hq
def solution(scoville, K):
    hq.heapify(scoville)
    cnt = 0
    while len(scoville) > 1 and scoville[0] < K:
        min1 = hq.heappop(scoville)
        min2 = hq.heappop(scoville)
        hq.heappush(scoville, min1 + min2*2)
        cnt += 1
    return cnt if scoville[0] >= K else -1


# 1회차 코드
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) >= 2 and scoville[0] < K:
        num1 = heapq.heappop(scoville)
        num2 = heapq.heappop(scoville)
        heapq.heappush(scoville,(num1 + num2*2))
        cnt += 1

    return cnt if all(num >= K for num in scoville) else -1