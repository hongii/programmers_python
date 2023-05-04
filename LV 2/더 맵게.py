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