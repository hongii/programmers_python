import math
def solution(fees, records):
    inCars = {}
    total = {}
    res = []
    for x in records:
        times = int(x[:2])*60 + int(x[3:5])
        car, state = x[6:10], x[11:]

        if car not in total.keys(): # 자동차의 누적 시간
            total[car] = 0

        if car not in inCars.keys():
            inCars[car] = times
        elif car in inCars.keys() and state == "OUT":
            total[car] += times - inCars[car]
            del(inCars[car])

    # 출차하지 않은 차들
    for car, time in inCars.items():
        total[car] += (23*60 + 59) - time

    [baseTime, baseFee, perTime, perFee] = [x for x in fees]
    for car, times in total.items():
        if times < baseTime:
            res.append([car, baseFee])
        else:
            res.append([car, baseFee + math.ceil((times-baseTime)/perTime)*perFee])

    res.sort(key=lambda x:x[0])
    return [x[1] for x in res]