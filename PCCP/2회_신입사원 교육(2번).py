import heapq
def solution(ability, number):
    heapq.heapify(ability)
    
    while number:
        min1 = heapq.heappop(ability)
        min2 = heapq.heappop(ability)
        heapq.heappush(ability, min1+min2)
        heapq.heappush(ability, min1+min2)
        number -= 1
    return sum(ability)