def solution(n):
    answer = []
    numStr = str(n)
    answer = list(map(int,list(numStr)))
    answer.reverse()
    return answer