def solution(food):
    res = ""
    for i in range(1, len(food)):
        cnt = food[i]//2
        res += str(i) * cnt
    res += "0" + res[::-1]
    return res
        