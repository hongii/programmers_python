def solution(order):
    subBelt = []
    cnt = 0
    i = 0  
    for num in range(1, len(order)+1):
        if num != order[i]:
            subBelt.append(num)
        else:
            cnt += 1
            i += 1
            
        while subBelt:
            if subBelt[-1] == order[i]:
                cnt += 1
                i += 1
                subBelt.pop()
            else:
                break
    return cnt