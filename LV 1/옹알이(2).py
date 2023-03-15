# 다시 풀어볼 문제
def solution(babbling):
    cnt = 0
    words = ["aya", "ye", "woo", "ma"]
    for x in babbling:
        for word in words:
            if word*2 not in x:
                x = x.replace(word, " ")
        if x.strip() == "":
            cnt += 1
    return cnt

