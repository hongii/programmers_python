import heapq
def solution(operations):
    hq = []
    for ops in operations:
        op, num = ops.split(" ")
        if op == "I":
            heapq.heappush(hq, int(num))
        elif hq and op == "D":
            if int(num) == 1:
                hq.remove(max(hq))
                heapq.heapify(hq)
            elif int(num) == -1:
                heapq.heappop(hq)
                
    if not hq:
        return [0, 0]
    else:
        return [max(list(hq)), hq[0]]