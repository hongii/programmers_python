def solution(n):
    answer = 0
    numStr = str(n)
    numList = list(numStr)
    for i in range(len(numList)):
        answer += int(numList[i])
    print(answer)

    return answer