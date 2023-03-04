def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    return int("".join(n))

# 최적의 풀이와 동일! 