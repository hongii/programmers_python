def solution(participant, completion):
    dic = {}
    for name in participant:
        if name not in dic.keys():
            dic[name] = 1
        else:
            dic[name] += 1
    
    for name in completion:
        if dic[name] > 1:
            dic[name] -= 1
        else:
            del dic[name]
    answer = list(dic.keys())       
    return answer[0]

''' 
# collection모듈의 Counter함수 사용법
1. 문자열을 넣는 경우 -> 문자열을 구성하는 알파벳의 사용빈도를 알 수 있다.
ex)
value = "Hello Appia"
print(Counter(value)) -> 출력 결과: Counter({'l': 2, 'p': 2, 'H': 1, 'e': 1, 'o': 1, ' ': 1, 'A': 1, 'i': 1, 'a': 1})

2. 문자열 리스트를 넣는 경우 -> 각 문자열의 사용빈도를 알 수 있다.
ex)
list = ['Hello', 'HI', 'How', 'When', 'Where', 'Hello']
print(Counter(list)) -> 출력 결과: Counter({'Hello': 2, 'HI': 1, 'How': 1, 'When': 1, 'Where': 1})
'''

''' Counter를 이용한 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''