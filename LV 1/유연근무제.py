def solution(schedules, timelogs, startday):
    def to_seconds(t):
        return (t//100)*60 + t%100
    
    arrive_times = [to_seconds(t)+10 for t in schedules]
    cnt = 0
    for i, times in enumerate(timelogs):
        day = startday
        flag = True
        
        for t in times:
            if day == 6 or day == 7:
                day = (day + 1)%7 or 7
                continue
            if to_seconds(t) > arrive_times[i]:
                flag = False
                break
            day = (day + 1)%7 or 7
        
        if flag:
            cnt += 1
    
    return cnt