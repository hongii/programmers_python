def solution(absolutes, signs):
    answer = []
    for i in range(len(absolutes)):
        if signs[i]:
            signNum = absolutes[i]
        else:
            signNum = -absolutes[i]
        answer.append(signNum)
    return sum(answer)
