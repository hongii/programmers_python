def solution(a, b):
    if a > b:
        a, b = b, a
    numList = [i for i in range(a, b+1)]
    return sum(numList)

''' 최적의 풀이 -> 굳이 list를 만들지 않아도, range()함수를 사용하면 a~b까지의 정수 범위를 반환하기 때문에 iterable하므로, 바로 sum()함수를 이용하여 합을 구할 수 있다.
def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
'''