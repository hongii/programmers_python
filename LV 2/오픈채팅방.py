def solution(record):
    enter = {}
    info, res = [], []
    for r in record:
        info = r.split(" ")
        if info[0] == "Enter":
            enter[info[1]] = info[2]
        elif info[0] == "Change":
            enter[info[1]] = info[2]

    for r in record:
        info = r.split(" ")
        if info[0] == "Enter":
            res.append(enter[info[1]]+"님이 들어왔습니다.")
        elif info[0] == "Leave":
            res.append(enter[info[1]]+"님이 나갔습니다.")

    return res