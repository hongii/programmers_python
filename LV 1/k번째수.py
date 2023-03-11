def solution(array, commands):
    res = []
    for arr in commands:
        i, j, k = arr # i, j, k = arr[0], arr[1], arr[2] 로 안해도 됨 -> 파이썬 구조분해할당
        tmp = array[i-1:j]
        tmp.sort()
        res.append(tmp[k-1])
    return res

