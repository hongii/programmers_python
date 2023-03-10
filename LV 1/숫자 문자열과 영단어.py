def solution(s):
    if "zero" in s:
        s = s.replace("zero", "0")
    if "one" in s:
        s = s.replace("one", "1")
    if "two" in s:
        s = s.replace("two", "2")
    if "three" in s:
        s = s.replace("three", "3")
    if "four" in s:
        s = s.replace("four", "4")
    if "five" in s:
        s = s.replace("five", "5")
    if "six" in s:
        s = s.replace("six", "6")
    if "seven" in s:
        s = s.replace("seven", "7")
    if "eight" in s:
        s = s.replace("eight", "8")
    if "nine" in s:
        s = s.replace("nine", "9")
    return int(s)

'''
# replace()에 관련하여 잘못 알고 있던 문법 -> replace()함수에 3번째 인자 값인 count 값을 적어주지 않으면 문자열 전체를 변경한다.
즉, "zero234sevenzerozero".replace("zero", "0")의 경우 -> "0234seven00"이 반환된다.
"zero"라는 문자열이 존재하는 부분을 전부 "0"으로 치환한다. (가장 먼저 위치하는 "zero"만 변경하는 것이 아님!)
ex1. replace("zero", "0", 2) -> 문자열 앞에서 부터 "zero"를 "0"으로 2회 변경한다. 즉, "0234seven0zero"이 반환된다.
'''

'''딕셔너리를 이용한 풀이
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

'''