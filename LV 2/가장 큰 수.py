# 풀이 참고 -> 문자열을 4번 반복해서 문자열 슬라이싱으로 index 0~3 까지 비교(key=lambda x:(x*4)[:4])
# (numbers의 원소는 0이상 1000이하의 값으로 조건이 주어졌으므로 한 자릿수 숫자의 경우 같은수를 4번 반복하여 최소길이 4자릿수로 만들기위함)
def solution(numbers):
    numbers = [str(x) for x in numbers] # 각 원소를 문자열로 만들어 줘야함 -> 숫자형 값 비교가 아닌 문자열 값 비교를 하기 위해
    numbers.sort(key=lambda x:(x*4)[:4], reverse=True)
    return "".join(numbers) if int("".join(numbers)) != 0 else "0"

'''
첫번째풀이 -> 시간초과 
from itertools import permutations
def solution(numbers):
    numbers = [str(x) for x in numbers]
    pm = list(permutations(numbers, len(numbers)))

    maxNum = 0
    for num in pm:
        num = "".join(list(num))
        if int(num) > maxNum:
            maxNum = int(num)
    return str(maxNum)
'''