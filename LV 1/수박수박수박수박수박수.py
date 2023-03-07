def solution(n):
    str = ""
    for i in range(1, n+1):
        if i % 2 == 1:
            str += "수"
        else:
            str += "박"
    return str