def solution(n):
    answer = []
    numStr = str(n)
    answer = list(map(int,list(numStr)))
    answer.reverse()
    return answer

# 최적의 풀이 : 입력받은 int숫자형을 string으로 변환해서 reversed()함수 이용 (입력받은 숫자가 문자열 형태로 뒤집힌다.)
#               -> map 함수를 통해 뒤집힌 문자열을 int형으로 변환 후 리스트로 만든다.
def digit_reverse(n):
    return list(map(int, reversed(str(n))))