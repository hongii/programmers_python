def solution(n):
    answer = float(n ** (1/2))
    if answer == int(answer):
        return (int(answer)+1)**(2)
    else:
        return -1