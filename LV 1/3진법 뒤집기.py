def solution(n):
    reversedTernary = []
    while n != 0:
        reversedTernary.append(n%3) # 이렇게 넣으면 뒤집은 3진법이 바로 들어가진다.
        n = n//3

    res, exp = 0, 0
    for i in range(len(reversedTernary)-1, -1, -1):
        res += reversedTernary[i] * (3**exp)
        exp += 1
    return res

'''최적의 풀이 -> string형으로 저장한 뒤집은 3진법을 바로 int(string, base)함수로 취하면, string 값을 base진법으로 출력된다.
def solution(n):
    reversedTernary = ""
    while n != 0:
        reversedTernary += str(n%3)
        n = n//3
    res = int(reversedTernary, 3)
    return res


'''