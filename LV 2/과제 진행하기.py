def solution(plans):
    plans.sort(key=lambda x:(int(x[1][:2])*60 + int(x[1][3:])))
    doing, stop, res = [], [], []
    for i in range(len(plans)):
        name, start, playtime = plans[i][0], plans[i][1], int(plans[i][2])
        start = int(start[:2])*60 + int(start[3:])
        if not doing:
            doing.append((name, start,playtime))
        else:
            # 새로운 과제는 이미 진행중이던 과제가 있더라도 무조건 바꿔치기 돼야함. 진행중이던 과제의 수행시간이 아직 남았으면 stop으로, 다끝났으면 res에 넣는 로직 반복
            now_name, now_start, now_pt = doing.pop()
            if now_start+now_pt > start: # 현재 진행중인 과제가 새로운 과제를 시작할 시간에 덜 끝난 상태라면 stop에 저장
                stop.append((now_name, now_pt-(start-now_start))) # 덜 끝난 과제는 stop에 넣음
                doing.append((name, start, playtime)) # 새로운 과제를 진행
            else: # 현재 새로운 과제를 수행해야 하는 시작시간에 진행중이던 과제가 이미 끝나있는 경우
                res.append(now_name) 
                time = start - (now_start+now_pt) # "새로운 과제의 시작시간 - 진행중이던 과제가 끝난 시간" => "새로운 과제의 시작시간 전까지 남은 시간"동안 stop에 보관된 과제 수행 가능
                while stop:
                    stop_name, stop_remainTime = stop.pop()
                    if time - stop_remainTime >= 0: # stop에 보관되어 있는 최신 과제가 남은 시간(time)동안 수행 가능한 경우
                        time -= stop_remainTime
                        res.append(stop_name)
                    else: # stop에 있던 최신 과제를 새로운 과제 시작하기 전까지의 남은 시간동안만 수행하고 다시 stop에 집어넣음
                        stop.append((stop_name, stop_remainTime-time))
                        break

                doing.append((name , start, playtime)) # 새로운 과제 진행

    res.append(doing[0][0])
    while stop:
        res.append(stop.pop()[0])
    return res