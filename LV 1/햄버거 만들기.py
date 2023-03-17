def solution(ingredient):
    cnt = 0
    burger = ""
    for x in ingredient:
        burger += str(x)
        if burger[-4:] == "1231":
            burger = burger[:-4]
            cnt += 1
    return cnt