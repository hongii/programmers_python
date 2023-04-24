def solution(s):
    cnt, removeTotal = 0, 0
    while s != "1":
        total = len(s)
        s = s.replace("0", "")
        removeZero = len(s)
        removeTotal += total - removeZero
        s = bin(removeZero)[2:]
        cnt += 1
        
    return [cnt, removeTotal]