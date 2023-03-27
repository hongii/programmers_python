import heapq as hq
def totalMins(startTime, endTime):  
    startMins = int(startTime[:2])*60 + int(startTime[3:])
    endMins = int(endTime[:2])*60 + int(endTime[3:]) + 10
    return startMins, endMins
    
def solution(book_time):
    rooms = []
    cnt, max_cnt = 0, 0
    book_time.sort()
    for i in range(len(book_time)):
        times = book_time[i]
        start, end = totalMins(times[0], times[1])
        
        if i == 0:
            hq.heappush(rooms, end)
            cnt, max_cnt = 1, 1
        else:
            while rooms:
                if rooms[0] > start:
                    hq.heappush(rooms, end)
                    cnt = len(rooms)
                    max_cnt = max(max_cnt, cnt)
                    break
                else:
                    hq.heappop(rooms)

    return max_cnt
